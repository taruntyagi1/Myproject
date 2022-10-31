from distutils.log import error
from enum import auto, unique
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise error("email is required")
        if not username:
            raise error("username is required")

        user = self.model(
            email = self.normalize_email('email'),
            first_name = first_name,
            last_name = last_name,
            username = username,

        )
        password = user.set_(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,username,emial,password=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email = self.normalize_email('email'),
            username=username,

        )
       

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        password = user.set_(password)
        return user


      
objects = UserManager()

class User(AbstractBaseUser):
    def create_user(self,first_name,last_name,username,email,password=None):
        OWNER = 1
        CUSTOMER = 2

        ROLE_CHOICE = (
            (OWNER , 'owner'),
            (CUSTOMER,'customer')
           )

        first_name = models.CharField(max_length = 20)
        last_name = models.CharField(max_length = 20)
        email = models.CharField(max_length = 50 ,unique = True)
        username = models.CharField(max_length = 20 , unique = True)
        phone_number =  models.CharField(max_length = 10, blank = True)
        role = models.PositiveSmallIntegerField(choices= ROLE_CHOICE, blank = True, null = True)



        date_joined = models.DateTimeField(auto_now_add = True)
        last_login = models.DateTimeField(auto_now_add = True)
        created_date = models.DateTimeField(auto_now_add = True)
        modified_date = models.DateField(auto_now_add = True)
        is_admin = models.BooleanField(default = False)
        is_active = models.BooleanField(default = False)
        is_staff = models.BooleanField(default = False)
        is_superadmin = models.BooleanField(default = False)    


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['username','phone_number','password']


def __str__(self):
    return self.email

def has_perm(self,perm,obj = None):
    return User.is_admin

def has_module_perms(self,app_label):
    return True