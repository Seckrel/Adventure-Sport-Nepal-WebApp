from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Faq
from .serializers import FaqSerializer
import json

# Create your views here.
class ShowAll(APIView):
    serializer_class = FaqSerializer
    def get(self, request):
        queryset = Faq.objects.all()
        objects = self.serializer_class(queryset[0]).data
        print(json.dumps(objects, indent=4))