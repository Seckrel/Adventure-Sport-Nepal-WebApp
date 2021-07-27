from django.db import models


class Hook(models.Model):
    hook_title = models.CharField(max_length=50)
    hook_text = models.TextField()
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE, default=None)


class ExpeditionInfo(models.Model):
    expedition_title = models.CharField(max_length=50)
    expedition_description = models.TextField()
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE, default=None)


class PricingInfo(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_date = models.DateTimeField()
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE, default=None)


class ItineraryInfo(models.Model):
    trek = models.ForeignKey('Trek', on_delete=models.CASCADE)
    start = models.PositiveIntegerField()
    end = models.PositiveIntegerField()
    itinerary_description = models.TextField()


class PackageInclusion(models.Model):
    inclusion_decription = models.TextField()
    trek = models.ForeignKey('Trek', on_delete=models.CASCADE)


class PackageExclusion(models.Model):
    exclusion_decription = models.TextField()
    trek = models.ForeignKey('Trek', on_delete=models.CASCADE)


class Trek(models.Model):
    package_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.package_name
