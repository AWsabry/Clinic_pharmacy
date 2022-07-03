from pharmacy.models import Medcine, Roshetta
from rest_framework import serializers


# class TestSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Testing_API
#         fields = ['id','name','is_active',]

class RoshettaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roshetta
        fields = '__all__'
class MedcineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcine
        fields = ['name',"Generic_Name", "price", 'type',
                    "stock", "id", "created", "active",]
