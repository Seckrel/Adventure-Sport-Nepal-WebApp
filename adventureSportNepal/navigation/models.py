from django.db import models
from trek.models import Trek
from ski.models import Ski
# Create your models here.


class TrekNav(models.Model):
    trek_nav_item = models.ForeignKey(Trek, on_delete=models.CASCADE, default= None)

class SkiNav(models.Model):
    ski_nav_item = models.ForeignKey(Ski, on_delete=models.CASCADE, default= None)
    
