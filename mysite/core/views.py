from genericpath import exists
from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, UserSerializer, UserSerializerWithToken
from rest_framework.generics import ListCreateAPIView
from .models import Customer, Company


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class CustomerCreate(ListCreateAPIView):
    print('yrk')
    serializer_class = CustomerSerializer
    permisson_classes = (permissions.AllowAny,)

    def get_queryset(self):
        return Customer.objects.filter(username = self.kwargs.get('username'))

    def perform_create(self, serializer):
        data = self.request.data
        company = Company.objects.filter(name = self.request.data['company'])
        if not company:
            company = Company.objects.create(name = self.request.data['company']) 
        new = Customer.objects.create(
                    username = data['username'],
                    password = data['password'],
                    firstName = data['firstName'],
                    lastName = data['lastName'],
                    company = data['company']
        )
        new.save()
        serializer = CustomerSerializer(new)
        return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)