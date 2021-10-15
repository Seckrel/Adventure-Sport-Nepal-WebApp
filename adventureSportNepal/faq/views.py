from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Faq
from .serializers import FaqSerializer
from rest_framework import status
import json

# Create your views here.


class ShowAll(APIView):
    serializer_class = FaqSerializer

    def get(self, request):
        queryset = Faq.objects.all()
        response = {
            "faqPackages": [

            ]
        }
        for query_item in queryset:
            response['faqPackages'].append(self.serializer_class(query_item).data)
        return Response(response, status=status.HTTP_200_OK)
