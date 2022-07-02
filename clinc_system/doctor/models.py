from django.db import models

from patient.models import Profile

# Create your models here.


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



class Medcine(models.Model):
    name = models.CharField(max_length=250, blank=True)
    Generic_Name = models.CharField(max_length=250, blank=True)
    type = models.CharField(max_length=250, blank=True)
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
