from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        """
        To make email login case sensetive.
        """
        
        return self.get(email__iexact=username)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        
        if not email:
            raise ValueError('Email does not included!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(email=email, password=password, **extra_fields)

class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    Age = models.CharField(max_length=10, null=True,blank=True)
    city = models.CharField(max_length=60, null=True,blank=True)
    PhoneNumber =  models.CharField(max_length=20, null=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    ProfilePic = models.ImageField(upload_to="profile/", null=True,blank=True)
    Are_you_deaf = models.CharField(max_length=300, null=True,blank=True)
    Question_02 = models.CharField(max_length=300, null=True,blank=True)
    Question_03 = models.CharField(max_length=300, null=True,blank=True)


    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class Appointment(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(verbose_name='Email')
    what_for = models.TextField(blank=True)
    PhoneNumber =  models.CharField(max_length=30, )
    date = models.CharField(max_length=30)    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Appointments"
