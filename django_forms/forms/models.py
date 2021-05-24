from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20, null=True)
    lastName = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100, null=True)
    student = 'st'
    teacher = 'te'
    TYPE_OF_USER = [
        (student, 'Student'),
        (teacher, 'Teacher'),
    ]
    typeUser = models.CharField(max_length=2, choices=TYPE_OF_USER)
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)