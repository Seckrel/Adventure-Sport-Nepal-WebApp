from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trek
from .serializers import TrekSerializer
from rest_framework import status
import json

# Create your views here.


class ShowAll(APIView):
    serializer_class = TrekSerializer

    def get(self, request):
        queryset = Trek.objects.all()
        response = {
            "trekPackages": [

            ]
        }
        for query_item in queryset:
            response['trekPackages'].append(
                self.serializer_class(query_item).data)
        return Response(response, status=status.HTTP_200_OK)


class ShowPackage(APIView):
    serializer_class = TrekSerializer

    def get(self, request, id):
        queryItem = Trek.objects.get(pk=id)
        response = {
            "trekPackage": {}
        }
        response['trekPackage'] = self.serializer_class(queryItem).data
        return Response(response, status=status.HTTP_200_OK)
