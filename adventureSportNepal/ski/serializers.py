from rest_framework import serializers
from .models import *


def CustomSlugRelatedField(field):
    return serializers.SlugRelatedField(
        many=True, read_only=True,
        slug_field=field
    )


class HookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hook
        exclude = ('id', 'ski')


class ExpeditionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpeditionInfo
        exclude = ('id', 'ski')


class PricingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingInfo
        exclude = ('id', 'ski')


class ItineraryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItineraryInfo
        exclude = ('id', 'ski')


class PackageInclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageInclusion
        exclude = ('id', 'ski')


class PackageExclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageExclusion
        exclude = ('id', 'ski')


class SkiSerializer(serializers.ModelSerializer):
    hook = HookSerializer()
    expedition_info = ExpeditionInfoSerializer()
    pricing_info = PricingInfoSerializer()
    itinerary_info = ItineraryInfoSerializer(many=True)
    package_inclusion = CustomSlugRelatedField('inclusion_decription')
    package_exclusion = CustomSlugRelatedField('exclusion_decription')

    class Meta:
        model = Ski
        fields = ('id', 'package_name', 'hook', 'expedition_info', 'pricing_info',
                  'itinerary_info', 'package_inclusion', 'package_exclusion')
