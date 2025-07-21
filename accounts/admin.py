from django.contrib import admin

from accounts.models import CustomerUser, Student

# Register your models here.

admin.site.register(CustomerUser)
admin.site.register(Student)