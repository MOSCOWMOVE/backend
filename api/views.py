from rest_framework import generics
from rest_framework.response import Response

from .serializers import MapSerializer, MoscowDistrictSerializer, GroupSerializer, SportZoneSerializer, \
    DepartmentalOrganizationSerializer, GroupInfoSerializer, SportTypeSerializer
from map_operations.models import Map, Group
from person_density.models import MoscowDistrict
from sport_objects.models import Accessibility, SportZone, DepartmentalOrganisation, OpenedType, SportType
from .getStats import get_stats_from_ids


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
            if "__all__" in types:
                res = res.objects.all()
            else:
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
            res = res.filter(organization__name__in=dep_name.split(","))
        except KeyError:
            pass

        try:
            opened_types = self.request.query_params["opened_types"].split(",")
            res = res.filter(open_type__name__in=opened_types)
        except KeyError:
            pass
        return res


class DepartmentOrgDetail(generics.RetrieveAPIView):
    serializer_class = DepartmentalOrganizationSerializer
    queryset = DepartmentalOrganisation.objects.all()


class GroupSportObject(generics.RetrieveAPIView):
    serializer_class = GroupSerializer

    def get(self, request, *args, **kwargs):
        print(self.request.query_params["ids"].split(","))
        Map.objects.all()[0].group_object(self.request.query_params["ids"].split(","))
        return Response(200)


class GetInfoFromZones(generics.RetrieveAPIView):
    serializer_class = GroupInfoSerializer

    def get(self, *args, **kwargs):
        return Response(
            data=get_stats_from_ids(self.request.query_params["ids"])
        )


class GetInfoFromGroup(generics.RetrieveAPIView):
    serializer_class = GroupInfoSerializer

    def get(self, *args, **kwargs):
        return Response(
            data=get_stats_from_ids(list(
                map(lambda x: x.zone_id,
                    Group.objects.get(id=self.request.query_params["id"]).sport_zones.all()
                    )
                )
            )
        )


class GetSportZone(generics.RetrieveAPIView):
    serializer_class = SportZoneSerializer

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        return Response(
            data=SportZoneSerializer(SportZone.objects.get(zone_id=pk)).data
        )


class SportTypes(generics.ListAPIView):
    serializer_class = SportTypeSerializer
    queryset = SportType.objects.all()


class GetSportType(generics.RetrieveAPIView):
    serializer_class = SportTypeSerializer
    queryset = SportType.objects.all()


class DepOrgs(generics.ListAPIView):
    serializer_class = DepartmentalOrganizationSerializer
    queryset = DepartmentalOrganisation.objects.all()