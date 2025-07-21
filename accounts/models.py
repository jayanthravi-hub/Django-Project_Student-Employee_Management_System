from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# create  CustomerUser and it is inherit from AbstarctionUser.
class CustomerUser(AbstractUser):
    ROLE_CHOICES = [('admin','Admin'),   #first value will store in db and 2nd value will display in the form
                    ('sales','Sales')]
    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default='sales')


class Student(models.Model):
    added_by = models.ForeignKey(CustomerUser,blank=True,null=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,unique=True)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    skillset=models.CharField(max_length=200)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.name