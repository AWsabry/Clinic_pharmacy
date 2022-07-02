from pharmacy.models import Medcine, Testing_API
from rest_framework import serializers


# class TestSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Testing_API
#         fields = ['id','name','is_active',]



class MedcineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcine
        fields = ['name',"Generic_Name", "price", 'type',
                    "stock", "id", "created", "active",]
