from django.contrib import admin
from patient.models import Appointment, Profile

# Register your models here.


class Register(admin.ModelAdmin):
    list_filter = ("email","first_name", "last_name", "last_modified")
    list_display = ("email","first_name", 'last_name','last_modified','PhoneNumber','is_active','is_doctor','is_superuser'
                  )
    search_fields = ['email']




class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ("name", "date",)
    list_display = ('email',"name","what_for", "date", "id",)
    search_fields = ['name']




admin.site.register(Profile, Register)
admin.site.register(Appointment,AppointmentAdmin)
