from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from trek.models import Trek
from ski.models import Ski
import json


class NavigationList(APIView):
    def get(self, request):
        print('\n\n\n******running****\n\n\n')
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

        return Response(objects, status=status.HTTP_200_OK)
