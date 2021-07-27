from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import datetime


class Hook(models.Model):
    hook_title = models.CharField(max_length=50)
    hook_description = models.TextField()
    ski = models.OneToOneField('ski', on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Catchy Hook for expedition"

    def __str__(self):
        return self.hook_title


class ExpeditionInfo(models.Model):
    expedition_title = models.CharField(max_length=50)
    expedition_description = models.TextField()
    ski = models.OneToOneField(
        "ski", on_delete=models.CASCADE, default=None, related_name="expedition_info")

    class Meta:
        verbose_name = "Title of the Expedition with short description"

    def __str__(self):
        return self.expedition_title


class PricingInfo(models.Model):
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price in USD",
        validators=[MinValueValidator(0.01)])
    # to validate
    available_date = models.DateField(verbose_name="Available Date (A.D.)")
    ski = models.OneToOneField(
        'ski', on_delete=models.CASCADE, default=None, related_name="pricing_info")

    class Meta:
        verbose_name = "Price of the package and nearest available date for it"
        constraints = [
            models.CheckConstraint(check=models.Q(
                price__gte=0), name='price_gte_0'),

        ]

    def clean(self):
        date = self.available_date
        if date < datetime.date.today():
            raise ValidationError('Available date cannot be in the past')

    def __str__(self):
        return f"$ {self.price} available at {self.available_date}"


class ItineraryInfo(models.Model):
    ski = models.ForeignKey(
        "Ski", on_delete=models.CASCADE, related_name="itinerary_info")
    # to validate
    start = models.PositiveIntegerField(verbose_name="Start Day")
    end = models.PositiveIntegerField(verbose_name="End Day", blank=True)
    itinerary_description = models.TextField()

    class Meta:
        verbose_name = "List Itinerary info about this package"

    def clean(self):
        if self.end < self.start:
            raise ValidationError('End day cannot be smaller than start')

    def save(self, *args, **kwargs):
        if not self.end:
            self.end = self.start
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Day ({self.start} to {self.end})"


class PackageInclusion(models.Model):
    ski = models.ForeignKey('ski', on_delete=models.CASCADE,
                            default=None, related_name="package_inclusion")
    inclusion_decription = models.TextField()

    class Meta:
        verbose_name = "List what is included in ski package"
        verbose_name_plural = "List what are included in ski package"

    def __str__(self):
        return f"Included {self.id}"


class PackageExclusion(models.Model):
    ski = models.ForeignKey('ski', on_delete=models.CASCADE,
                            default=None, related_name="package_exclusion")
    exclusion_decription = models.TextField()

    class Meta:
        verbose_name = "List what is excluded in ski package"
        verbose_name_plural = "List what are excluded in ski package"

    def __str__(self):
        return f"Excluded {self.id}"


class Ski(models.Model):
    package_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Ski Expedition Package"
        verbose_name_plural = "Ski Expedition Packages"

    def __str__(self):
        return self.package_name
