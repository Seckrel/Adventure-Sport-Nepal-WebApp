from django.db import models


class Hook(models.Model):
    hook_title = models.CharField(max_length=50)
    hook_description = models.TextField()
    ski = models.OneToOneField('ski', on_delete=models.CASCADE, default=None)


class ExpeditionInfo(models.Model):
    expedition_title = models.CharField(max_length=50)
    expedition_description = models.TextField()
    ski = models.OneToOneField(
        "ski", on_delete=models.CASCADE, default=None)


class PricingInfo(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_date = models.DateTimeField()
    ski = models.OneToOneField(
        'ski', on_delete=models.CASCADE, default=None)


class ItineraryInfo(models.Model):
    ski = models.ForeignKey("Ski", on_delete=models.CASCADE)
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField()
    itinerary_description = models.TextField()


class PackageInclusion(models.Model):
    ski = models.ForeignKey('ski', on_delete=models.CASCADE, default=None)
    inclusion_decription = models.TextField()


class PackageExclusion(models.Model):
    ski = models.ForeignKey('ski', on_delete=models.CASCADE, default=None)
    exclusion_decription = models.TextField()


class Ski(models.Model):
    package_name = models.CharField(max_length=200, unique=True)
