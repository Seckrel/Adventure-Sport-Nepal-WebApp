from rest_framework import serializers
from trek.models import Trek
from ski.models import Ski


class TrekNavSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='package_name')
    href = serializers.SerializerMethodField()

    class Meta:
        model = Trek
        fields = ('id', 'name', 'href')

    def get_href(self, obj):
        return f"ski/{obj.id}"


class SkiNavSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='package_name')
    href = serializers.SerializerMethodField()

    class Meta:
        model = Ski
        fields = ('id', 'name', 'href')

    def get_href(self, obj):
        return f"ski/{obj.id}"
