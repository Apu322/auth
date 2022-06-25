from django.urls import path
from .views import current_user, UserList, CustomerCreate

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('customer/<str:username>/', CustomerCreate.as_view()),
    path('customer/', CustomerCreate.as_view())
]