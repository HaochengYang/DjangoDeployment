from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9._-]+\.[a-zA-z]+$')

class UserManager(models.Manager):
    def add_user(self, postData):
        print postData

        errors = []

        if not postData['first_name']:
            errors.append('First name field is required')
        if len(postData['first_name']) < 2:
            errors.append('First name must be at least 2 characters long.')
        if not postData['last_name']:
            errors.append('Last name field is required')
        if len(postData['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long.')
        if not postData['email']:
            errors.append('Email field is required')
        if not EMAIL_REGEX.match(postData['email']):
            errors.append('Enter a valid email')
        if not postData['password']:
            errors.append('Password is required')
            errors.append('Password must match')
        if not postData['date_of_birth']:
            errors.append('Enter Your date of birth')

        user = self.filter(email=postData['email'])
        if user:
            errors.append('Email already exists')

        response = {}

        if errors:
            response['status'] = False
            response['errors'] = errors

        else:
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            new_user = self.create(first_name = postData['first_name'],
                        last_name = postData['last_name'],
                        email = postData['email'],
                        password = password,
                        date_of_birth = postData['date_of_birth']
            )
            response['status'] = True
            response['new_user'] = new_user

        return response

    def check_user(self, postData):
        user = self.filter(email=postData['email'])
        errors = []
        response = {}
        if user:
           #validate User login information
           #bcrypt.checkpw(postData['password'].encode(), bcrypt.gensalt())
           if bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) == user[0].password.encode():
               print("It Matched")
               response['status'] = True
               response['login_user'] = user[0]
           else:
               print("It Does Not Match")
               errors.append('Invalide email/password combinnation')
               response['status'] = False
               response['login_user'] = errors
        else:
           #email does not exists in database
           errors.append('Email does not exist.')
           response['status'] = False
           response['login_user'] = errors

        return response


class User(models.Model):
     first_name = models.CharField(max_length=55)
     last_name = models.CharField(max_length=55)
     email = models.EmailField()
     password = models.CharField(max_length=55)
     confirm_password = models.CharField(max_length=55)
     date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
     objects = UserManager()
