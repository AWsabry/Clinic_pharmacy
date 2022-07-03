import imp
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from html5lib import serialize
from sqlalchemy import true

# from pharmacy.serializers import TestSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pharmacy.models import Roshetta

from pharmacy.serializers import RoshettaSerializer
# Create your views here.


def index(request):
    return render(request, 'index.html',)

@api_view(['GET','POST'])
def get_roshetta(request):
    if request.method == 'GET':
        all = Roshetta.objects.all()
        print("hehe")
        serializer = RoshettaSerializer(all,many = True)
        print("hahah")
        return JsonResponse({"roshettas": serializer.data}, safe=False)
    if request.method == 'POST':
        serializer = RoshettaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
