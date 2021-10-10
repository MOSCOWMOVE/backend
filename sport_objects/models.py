from django.db import models


class DepartmentalOrganisation(models.Model):
    name = models.TextField()
    dep_id = models.TextField(unique=True)


class Accessibility(models.Model):
    name = models.TextField()
    distance = models.IntegerField()


class SportType(models.Model):
    name = models.TextField()


class SportZone(models.Model):
    organization = models.ForeignKey(DepartmentalOrganisation, on_delete=models.CASCADE)
    accessibility = models.ForeignKey(Accessibility, on_delete=models.CASCADE)
    sportTypes = models.ManyToManyField(SportType)
    name = models.TextField()
