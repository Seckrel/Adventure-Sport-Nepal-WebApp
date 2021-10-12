from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ski
from .serializers import SkiSerializer
from rest_framework import status
import json

# Create your views here.


class ShowAll(APIView):
    serializer_class = SkiSerializer

    def get(self, request):
        queryset = Ski.objects.all()
        response = {
            "skiPackages": [

            ]
        }
        for query_item in queryset:
            response['skiPackages'].append(
                self.serializer_class(query_item).data)
        return Response(response, status=status.HTTP_200_OK)


class ShowPackage(APIView):
    serializer_class = SkiSerializer

    def get(self, request, id):
        queryItem = Ski.objects.get(pk=id)
        response = {
            "skiPackage": {}
        }
        response['skiPackage'] = self.serializer_class(queryItem).data
        return Response(response, status=status.HTTP_200_OK)
