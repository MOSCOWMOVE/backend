from django.db import models
from sport_objects.models import SportZone


class Group(models.Model):
    sport_zones = models.ManyToManyField(SportZone)
    name = models.TextField()


class Map(models.Model):
    flat_objects = models.ManyToManyField(SportZone)
    groups = models.ManyToManyField(Group)

    def group_object(self, objects_ids: [str]):
        for i in objects_ids:
            self.flat_objects.remove(SportZone.objects.get(zone_id=i))
        group = Group.objects.create(name="")
        for i in objects_ids:
            group.sport_zones.add(SportZone.objects.get(zone_id=i))
        self.groups.add(group)
