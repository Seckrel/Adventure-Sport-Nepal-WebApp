from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Trek
from .serializers import TrekSerializer
import json


class ShowAll(APIView):
    serializer_class = TrekSerializer
    def get(self, request):
        queryset = Trek.objects.all()
        objects = self.serializer_class(queryset[0]).data
        print(json.dumps(objects, indent=4))
