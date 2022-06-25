from django.db import models
from numpy import mafromtxt

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 100, unique = True)

    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name

class Customer(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    company = models.ForeignKey(Company, related_name = "company", on_delete = models.CASCADE)

    REQUIRED_FIELDS = ['username','password','firstName','lastName','company']

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.username
