from django.contrib import admin
from .models import *


class HookInline(admin.StackedInline):
    model = Hook


class ExpeditionInfoInline(admin.StackedInline):
    model = ExpeditionInfo


class PricingInfoInline(admin.StackedInline):
    model = PricingInfo


class ItineraryInfoInline(admin.TabularInline):
    model = ItineraryInfo


class PackageInclusionInline(admin.StackedInline):
    model = PackageInclusion


class PackageExclusionInline(admin.StackedInline):
    model = PackageExclusion


class TrekAdmin(admin.ModelAdmin):
    model = Trek
    inlines = [HookInline, ExpeditionInfoInline, PricingInfoInline,
               ItineraryInfoInline, PackageInclusionInline, PackageExclusionInline]


admin.site.register(Trek, TrekAdmin)