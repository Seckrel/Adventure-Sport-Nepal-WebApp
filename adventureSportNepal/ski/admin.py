from django.contrib import admin
from . models import *
# Register your models here.


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


class SkiAdmin(admin.ModelAdmin):
    model = Ski
    inlines = [HookInline, ExpeditionInfoInline, PricingInfoInline,
               ItineraryInfoInline, PackageInclusionInline, PackageExclusionInline]


admin.site.register(Ski, SkiAdmin)
