from django.db import models


class MoscowDistrict(models.Model):
    name = models.TextField()
    density = models.FloatField()