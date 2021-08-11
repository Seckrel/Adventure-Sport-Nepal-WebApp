from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from trek.models import Trek
from ski.models import Ski
import json


class NavigationList(APIView):
    print('running')
    def get(self, request):
        trek_queryset = Trek.objects.all()
        ski_queryset = Ski.objects.all()
        objects = {
            'trek': [],
            'ski': []
        }
        for query_item in trek_queryset:
            objects['trek'].append(TrekNavSerializer(query_item).data)

        for query_item in ski_queryset:
            objects['ski'].append(SkiNavSerializer(query_item).data)
        
        print(json.dumps(objects, indent=4))
