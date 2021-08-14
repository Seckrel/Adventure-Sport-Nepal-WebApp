from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from trek.models import Trek
from ski.models import Ski
import json


def CreatingReturnObject(expedition_item, query_set, serializer_class):
    objects = {
        'name': expedition_item,
        'items': []
    }
    for query_item in query_set:
        objects['items'].append(serializer_class(query_item).data)
    return objects


class NavigationList(APIView):
    def get(self, request):
        print('\n\n\n******running****\n\n\n')
        trek_queryset = Trek.objects.all()
        ski_queryset = Ski.objects.all()
        response = {
            "expeditionList": [

            ]
        }
        response['expeditionList'].append(CreatingReturnObject(
            "treking", trek_queryset, TrekNavSerializer))
        response['expeditionList'].append(CreatingReturnObject(
            "sking", ski_queryset, SkiNavSerializer))

        return Response(response, status=status.HTTP_200_OK)
