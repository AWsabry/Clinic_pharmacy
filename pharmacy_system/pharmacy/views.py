import imp
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from html5lib import serialize
from sqlalchemy import true

from pharmacy.models import Testing_API
# from pharmacy.serializers import TestSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return render(request, 'index.html',)

# @api_view(['GET','POST'])
# def testing(request):
#     if request.method == 'GET':
#         all = Testing_API.objects.all()
#         serializer = TestSerializers(all,many = True)
#         return JsonResponse({"Names": serializer.data}, safe=False)
#     if request.method == 'POST':
#         serializer = TestSerializers(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)

