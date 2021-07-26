from django.contrib import admin
from . models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.


class HookInline(admin.StackedInline):
    model = Hook


class ExpeditionInfoInline(admin.StackedInline):
    model = ExpeditionInfo


class PricingInfoInline(admin.StackedInline):
    model = PricingInfo


class ItineraryInfoInline(admin.TabularInline):
    model = ItineraryInfo


class PackageInclustionTypeInline(admin.StackedInline):
    model = PackageInclustionType


class SkiAdmin(admin.ModelAdmin):
    model = Ski
    inlines = [HookInline, ExpeditionInfoInline, PricingInfoInline,
               ItineraryInfoInline, PackageInclustionTypeInline]


admin.site.register(Ski, SkiAdmin)
