from typing import Any, Union

from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import (
    AbstractBaseUser , BaseUserManager, 
    PermissionsMixin , AnonymousUser, 
)

from server.target.models.abstracts import TimeStampedModel






class CompanySize(models.TextChoices):
    SMALL   = '11-50', '11-50'
    LARG    = '51-100', '51-100'
    X_LARG  = '101-500', '101-500'
    XX_LARG = '501-1000', '501-1000'
    More    = '1001', '1001'

class UserType(models.TextChoices):
    ADMIN       = 'ADMIN', 'ADMIN'
    JOB_SEEKER  = 'Job-Seeker', 'Job-Seeker'
    EMPLOYER    = 'Employer', 'Employer'



class TargetBaseUserManger(BaseUserManager):
    """This is the main class for user manger"""
    def create_user(self, email: str, password: str) -> 'User':
        """DMC method to create user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email: str, password: str):
        """ Create super user [admin] """
        user = self.create_user(
            email                   = self.normalize_email(email),
            password                = password,
        )
        user.is_admin               = True
        user.is_superuser           = True
        user.is_staff               = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    This model will be the base user table to inherit it in employer and job seeker tables
    """
    email           = models.EmailField(max_length=60, unique=True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    description     = models.TextField(max_length=255, null=True, blank=True)
    phone           = models.CharField(max_length=15, null=True, blank=True)
    user_type       = models.CharField(max_length=15, choices=UserType.choices, default=UserType.ADMIN)

    is_admin        = models.BooleanField(default = False)
    is_staff        = models.BooleanField(default = False)
    is_superuser    = models.BooleanField(default = False)
    is_active       = models.BooleanField(default = True)
    
    objects         = TargetBaseUserManger()
    USERNAME_FIELD  = 'email'
    
    @property
    def full_name(self) -> str:
        """Normal method to concatonate first_name and last_name"""
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm : str , obj:Union[models.Model, AnonymousUser, None]=None) -> bool:
        """For checking permissions. to keep it simple all admin have ALL permissons"""
        return self.is_admin
    
    @staticmethod
    def has_module_perms(app_label : Any) -> bool:
        """Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)"""
        return True

class JobSeeker(User):
    """Profile table of users that registered as a job seekers"""
    country = CountryField()
    city    = models.CharField(max_length=30)

    def __str__(self) -> str:
        """String method"""
        return self.full_name

class Employer(User):
    """Employer table of users that registered as a employers"""
    company_name = models.CharField(max_length=50)
    company_size = models.CharField(max_length=90, choices=CompanySize.choices, default=CompanySize.SMALL)

    def __str__(self) -> str:
        """String method"""
        return self.company_name