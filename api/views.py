from rest_framework import generics
from rest_framework.response import Response

from .serializers import MapSerializer, MoscowDistrictSerializer, GroupSerializer, SportZoneSerializer, \
    DepartmentalOrganizationSerializer
from map_operations.models import Map, Group
from person_density.models import MoscowDistrict
from sport_objects.models import Accessibility, SportZone, DepartmentalOrganisation


class MapDetails(generics.RetrieveAPIView):
    serializer_class = MapSerializer
    queryset = Map.objects.all()


class PersonDensity(generics.ListAPIView):
    serializer_class = MoscowDistrictSerializer
    queryset = MoscowDistrict.objects.all()


class GetGroups(generics.ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GetFlatSportZones(generics.ListAPIView):
    serializer_class = SportZoneSerializer
    queryset = Map.objects.all()[0].flat_objects.all()


class SortSportZoneByAccessibility(generics.ListAPIView):
    serializer_class = SportZoneSerializer

    def get_queryset(self):
        accessibility = self.request.query_params["accessibility"].split(",")
        filtered_zones = SportZone.objects.filter(
            accessibility__distance__in=accessibility)

        return filtered_zones


class SortZonesByListOfSportTypes(generics.ListAPIView):
    serializer_class = SportZoneSerializer

    def get_queryset(self):
        sport_types = self.request.query_params["sport_types"]
        print(sport_types)
        return SportZone.objects.filter(sportTypes__name__in=sport_types.split(","))


class SortSportZoneByName(generics.ListAPIView):
    serializer_class = SportZoneSerializer

    def get_queryset(self):
        name = self.request.query_params["name"]
        return SportZone.objects.filter(name__contains=name)


class SortSportByDepartmentName(generics.ListAPIView):
    serializer_class = SportZoneSerializer

    def get_queryset(self):
        dep_name = self.request.query_params["dep_name"]
        return SportZone.objects.filter(organization__name__contains=dep_name)


class SportZoneDetail(generics.RetrieveAPIView):
    serializer_class = SportZoneSerializer
    queryset = SportZone.objects.all()

    def get(self, *args, **kwargs):
        return Response(data=SportZoneSerializer(SportZone.objects.get(zone_id=kwargs.get("pk"))).data)


class SortZones(generics.ListAPIView):
    serializer_class = SportZoneSerializer

    def get_queryset(self):
        res = SportZone.objects.all()
        try:
            name = self.request.query_params["name"]
            res = res.filter(name__contains=name)
        except KeyError:
            pass

        try:
            types = self.request.query_params["types"].split(",")
            res = res.filter(sportTypes__name__in=types)
        except KeyError:
            pass

        try:
            accessibility = self.request.query_params["accessibility"].split(",")
            res = res.filter(accessibility__distance__in=accessibility)
        except KeyError:
            pass

        try:
            dep_name = self.request.query_params["dep_name"]
            res = res.filter(organization__name__contains=dep_name)
        except KeyError:
            pass

        return res


class DepartmentOrgDetail(generics.RetrieveAPIView):
    serializer_class = DepartmentalOrganizationSerializer
    queryset = DepartmentalOrganisation.objects.all()
