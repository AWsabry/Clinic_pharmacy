from doctor.models import Medcine, Medicine_items, Roshetta
from rest_framework import serializers



class MedcineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcine
        fields = ['name',"Generic_Name", "price", 'type',
                    "stock", "id", "created", "active",'description']


class RoshettaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roshetta
        fields = '__all__'