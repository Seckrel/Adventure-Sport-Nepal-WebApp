from rest_framework import serializers
from .models import *

class TrekNavSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='trek_nav_item')
    href = serializers.SerializerMethodField()

    class Meta:
        model = TrekNav
        fields = ('name', 'href')

    def get_href(self, obj):
        return f"/trek/{obj.id}"


class SkiNavSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='ski_nav_item')
    href = serializers.SerializerMethodField()

    class Meta:
        model = SkiNav
        fields = ('name', 'href')

    def get_href(self, obj):
        return f"/ski/{obj.id}"
