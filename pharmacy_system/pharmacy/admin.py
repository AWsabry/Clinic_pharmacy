from django.contrib import admin

from pharmacy.models import Company, Medcine, Profile, Testing_API
import requests

# Register your models here.



class Register(admin.ModelAdmin):
    list_filter = ("email","Pharmacy_Name", "last_modified")
    list_display = ("email","Pharmacy_Name",'last_modified','PhoneNumber','is_active','is_superuser'
                  )
    search_fields = ['email']



class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_filter = ("name", "created",)
    list_display = ('name', "created", "id",)
    search_fields = ['name']



class MedcineAdmin(admin.ModelAdmin):
    list_filter = ("name","Generic_Name", "company", "type", "created")
    list_display = ('name',"Generic_Name", "price", 'type', "company",
                    "stock", "id", "created", "active",)
    list_display_links = [
        'name',
        'company',
    ]
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        print('added')
            # Make the API call
        requests.post('http://127.0.0.1:8000/get_medcine/', json= {
            "name": obj.name,
            "Generic_Name": obj.Generic_Name,
            "price": obj.price,
            "type": obj.type,
            "stock": obj.stock,
            "created": obj.created,
            "active": obj.active})
        # Delegate the save to the parent class
        super().save_model(request, obj, form, change)



class Testing_API_admin(admin.ModelAdmin):
    list_filter = ("name", "is_active",)
    list_display = ("name", "is_active", "id",)
    search_fields = ['name']



admin.site.register(Profile, Register)
# admin.site.register(Testing_API, Testing_API_admin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Medcine, MedcineAdmin)
