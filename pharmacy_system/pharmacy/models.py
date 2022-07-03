from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin,Group

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



class Company(models.Model):
    name = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(unique=True, db_index=True)
    image = models.ImageField(upload_to="categories", blank=True)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)    
    testing_migration = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"



class Medcine(models.Model):
    name = models.CharField(max_length=250, blank=True)
    Generic_Name = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=250, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null= True,blank=True)
    price = models.FloatField(default=0)
    stock = models.IntegerField()
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Medcines"


class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    Pharmacy_Name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_pharmacist = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    Age = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=60, null=True, blank=True)
    PhoneNumber =  models.CharField(max_length=20, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    ProfilePic = models.ImageField(upload_to="profile/", null=True, blank=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email


class Disease(models.Model):
    name = models.CharField(max_length=250, blank=True)
    Scientifc_Name = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Diseases"



class Roshetta(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT,null= True,blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.PROTECT,null= True,blank=True)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image_01 = models.ImageField(upload_to="profile/", null=True,blank=True)
    image_02 = models.ImageField(upload_to="profile/", null=True,blank=True)


    def __str__(self):
        return 'Roshettas'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "Roshettas"



class Medicine_items(models.Model):
    medicine = models.ForeignKey(Medcine, on_delete=models.PROTECT,null= True,blank=True)  
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)    
    roshetta = models.ForeignKey(Roshetta, on_delete=models.PROTECT,null= True,blank=True)  

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Medicines_items"
