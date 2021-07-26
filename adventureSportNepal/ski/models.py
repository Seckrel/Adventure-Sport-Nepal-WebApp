from django.db import models

# Create your models here.


class Hook(models.Model):
    hook_title = models.CharField(max_length=50)
    hook_description = models.TextField()


class ExpeditionInfo(models.Model):
    expedition_title = models.CharField(max_length=50)
    expedition_description = models.TextField()


class PricingInfo(models.Model):
    price = models.DecimalField(decimal_places=2)
    available_date = models.DateTimeField()


class ItineraryInfo(models.Model):
    ski = models.ForeignKey(Ski, on_delete=models.CASCADE)
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField()
    itinerary_description = models.TextField()


class PakageInclusionDetail(models.Model):
    package_inclusion=models.ForeignKey(PackageInclusion, on_delete=models.CASCADE)
    description = models.TextField()

class PackageInclusion(models.Model):

    INCLUSION_TYPE = (
        ('Included', 0),
        ('Excluded', 1)
    )
    included_type = models.IntegerField(choices=INCLUSION_TYPE)



class Ski(models.Model):
    package_name = models.CharField(max_length=200, unique=True)
    hook = models.OneToOneField(Hook, on_delete=models.CASCADE)
    expedition = models.OneToOneField(ExpeditionInfo, on_delete=models.CASCADE)
    pricing_info = models.OneToOneField(PricingInfo, on_delete=models.CASCADE)
