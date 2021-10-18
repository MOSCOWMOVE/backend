from rest_framework import serializers


from sport_objects.models import SportZone, SportType, Position, Accessibility, DepartmentalOrganisation
from map_operations.models import Map, Group
from person_density.models import MoscowDistrict


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["latitude", "longitude"]


class SportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportType
        fields = ["name"]


class AccessibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessibility
        fields = ["distance", "name"]


class DepartmentalOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalOrganisation
        fields = ["name", "dep_id"]


class SportZoneSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = SportZone
        fields = ["position", "organization", "accessibility", "sportTypes", "name", "zone_id"]


class GroupSerializer(serializers.ModelSerializer):
    sport_zones = SportZoneSerializer(many=True)

    class Meta:
        model = Group
        fields = ["sport_zones", "name"]


class MapSerializer(serializers.ModelSerializer):
    flat_objects = SportZoneSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = Map
        fields = ["groups", "flat_objects"]


class MoscowDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoscowDistrict
        fields = ["name", "density"]


class GroupInfoSerializer(serializers.Serializer):
    sportTypes = SportTypeSerializer(many=True)
    square = serializers.IntegerField()
    polls = serializers.IntegerField()
    opened = serializers.IntegerField()
    closed = serializers.IntegerField()
