from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
import datetime


class Hook(models.Model):
    hook_title = models.CharField(max_length=50)
    hook_text = models.TextField()
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name = "Catchy Hook for expedition"

    def __str__(self):
        return self.hook_title


class ExpeditionInfo(models.Model):
    expedition_title = models.CharField(max_length=50)
    expedition_description = models.TextField()
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE,
                                default=None, related_name="expedition_info")

    class Meta:
        verbose_name = "Title of the Expedition with short description"

    def __str__(self):
        return self.expedition_title


class PricingInfo(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Price in USD",
                                validators=[MinValueValidator(0.01)])
    available_date = models.DateField(verbose_name="Available Date (A.D.)")
    trek = models.OneToOneField('Trek', on_delete=models.CASCADE,
                                default=None, related_name="pricing_info")

    class Meta:
        verbose_name = "Price of the package and nearest available date for it"
        constraints = [
            models.CheckConstraint(check=models.Q(
                price__gte=0), name='trek_price_gte_0'),
        ]

    def clean(self):
        date = self.available_date
        if date < datetime.date.today():
            raise ValidationError('Available date cannot be in the past')

    def __str__(self):
        return f"$ {self.price} available at {self.available_date}"


class ItineraryInfo(models.Model):
    trek = models.ForeignKey(
        'Trek', on_delete=models.CASCADE, related_name="itinerary_info")
    start = models.PositiveIntegerField(verbose_name="Start Day")
    end = models.PositiveIntegerField(
        verbose_name="End Day", blank=True, null=True)
    itinerary_description = models.TextField()

    class Meta:
        verbose_name = "List Ininerary info about this package"

    def clean(self):
        if self.end and self.end < self.start:
            raise ValidationError("End day cannot be smaller than start")

    def save(self, *args, **kwargs):
        if self.start == self.end:
            self.end = None
        super().save(*args, **kwargs)

    def __str__(self):
        if not self.end:
            return f"Day ({self.start})"
        return f"Day ({self.start} to {self.end})"


class PackageInclusion(models.Model):
    inclusion_decription = models.TextField()
    trek = models.ForeignKey('Trek', on_delete=models.CASCADE,
                             default=None, related_name="package_inclusion")

    class Meta:
        verbose_name = "List what is included in trek package"
        verbose_name_plural = "List what are included in trek package"

    def __str__(self):
        return f"Included {self.id}"


class PackageExclusion(models.Model):
    exclusion_decription = models.TextField()
    trek = models.ForeignKey('Trek', on_delete=models.CASCADE,
                             default=None, related_name="package_exclusion")

    class Meta:
        verbose_name = "List what is excluded in trek package"
        verbose_name_plural = "List what are excluded in trek package"

    def __str__(self):
        return f"Excluded {self.id}"


class Trek(models.Model):
    package_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Trek Expedition Package"
        verbose_name_plural = "Trek Expedition Packages"

    def __str__(self):
        return self.package_name
