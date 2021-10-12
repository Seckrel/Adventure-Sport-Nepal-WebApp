from django.db import models
from django.core.exceptions import ValidationError
from trek.models import Trek
from ski.models import Ski

MAX_NAV_ITEMS = 5

class TrekNav(models.Model):
    trek_nav_item = models.ForeignKey(Trek, on_delete=models.CASCADE, default= None)

    class Meta:
        verbose_name = "Trek packages to show in Navigation"

    def clean(self):
        trek_nav = TrekNav.objects.all()
        print(trek_nav.count())
        if (trek_nav.count() >= MAX_NAV_ITEMS):
            raise ValidationError("Cannot Add more than 5")
    
    def __str__(self):
        return str(self.trek_nav_item)

class SkiNav(models.Model):
    ski_nav_item = models.ForeignKey(Ski, on_delete=models.CASCADE, default= None)

    def clean(self):
        ski_nav = SkiNav.objects.all()
        if (ski_nav.count() >= MAX_NAV_ITEMS):
            raise ValidationError("Cannot Add more than 5.")

    def __str__(self):
        return str(self.ski_nav_item)
    
