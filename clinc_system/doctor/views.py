from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from doctor.models import Medcine, Roshetta
from doctor.serializers import MedcineSerializer, RoshettaSerializer

# Create your views here.

@api_view(['GET','POST'])

def get_medcine(request):
    if request.method == 'GET':
        all = Medcine.objects.all()
        serializer = MedcineSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = MedcineSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


def get_roshetta(request):
    if request.method == 'GET':
        all = Roshetta.objects.all()
        serializer = RoshettaSerializer(all,many = True)
        return JsonResponse({"roshettas": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = RoshettaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

