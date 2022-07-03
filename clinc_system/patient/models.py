from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from multiselectfield import MultiSelectField
from sqlalchemy import true

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


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    Age = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=20, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    ProfilePic = models.ImageField(upload_to="profile/", null=True, blank=True)

    Medical_Questions = (
        ("Angina", "Angina"),
        ("Fating fits", "Fating fits"),
        ("Hyper tension", "Hyper tension"),
        ("Coronary disease", "Coronary disease"),
        ("Diabetes", "Diabetes"),
        ("Stoke", "Stoke"),
        ("Any cardiac operatione", "Any cardiac operation"),
        ("Have faced a heart attack", "Have faced a heart attack"),
        ("Any chronic disease ", "Any chronic disease "),
    )

    currentComplaines = (
        ("Chest pain", "Chest pain"),
        ("Pain while making effort", "Pain while making effort"),
        ("Shortness of breath (difficulty in taking)", "Shortness of breath (difficulty in taking)"),
        ("Sweating", "Sweating"),
        ("Palpitation", "Palpitation"),
    )

    Do_you_suffer_from = MultiSelectField(choices=Medical_Questions,blank = True)
    Currentcomplains = MultiSelectField(choices=Medical_Questions,blank = True)
    Do_your_parents_suffer_from_blood_pressure  = models.BooleanField(default=False)
    Do_you_have_family_member_faced_early_or_sudden_death  = models.BooleanField(default=False)
    Do_you_have_family_member_with_heart_disease  = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class Appointment(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(verbose_name='Email')
    what_for = models.TextField(blank=True)
    PhoneNumber = models.CharField(max_length=30, )
    date = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Appointments"
