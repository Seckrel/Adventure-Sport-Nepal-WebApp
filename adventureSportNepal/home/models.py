from django.db import models

class Home(models.Model):
    landing_image_hook_text = models.CharField(max_length=25)

