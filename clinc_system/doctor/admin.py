from django.contrib import admin

from doctor.models import Disease, Medcine, Medicine_items, Roshetta
import requests



# Register your models here.







class DiseaseAdmin(admin.ModelAdmin):
    list_filter = ("name", "Scientifc_Name", "type", "created")
    list_display = ("name", "Scientifc_Name", 'type', 'created',
                    )
    search_fields = ['name']


class MedicineAdmin(admin.TabularInline):
    model = Medicine_items
    raw_id_fields = ['roshetta']


class RoshettaAdmin(admin.ModelAdmin):
    list_display = ("user", 'created', 'description')
    inlines = [
        MedicineAdmin,
    ]
    search_fields = ['user__email']

    def save_model(self, request, obj, form, change):
        print('added')
        # Make the API call
        requests.post('http://192.168.1.2:8080/get_roshetta/', json={
                    "description": obj.description,
                    "active": obj.active,
                    "created": obj.created,
                    })
        # Delegate the save to the parent class
        print('added_02')
        super().save_model(request, obj, form, change)


# admin.site.register(Doctor, DoctorAdmin)
# admin.site.register(Medicine_items)
admin.site.register(Medcine,)
admin.site.register(Roshetta, RoshettaAdmin)
admin.site.register(Disease, DiseaseAdmin)
