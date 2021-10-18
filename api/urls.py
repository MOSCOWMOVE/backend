from django.urls import path
from .views import MapDetails, PersonDensity, GetGroups, GetFlatSportZones, SortSportZoneByAccessibility, \
    SortZonesByListOfSportTypes, SortSportZoneByName, SortSportByDepartmentName, SportZoneDetail, SortZones, \
    DepartmentOrgDetail, GroupSportObject, GetInfoFromZones, GetInfoFromGroup, SportTypes


urlpatterns = [
    path("map/<pk>", MapDetails.as_view()),
    path("people_density", PersonDensity.as_view()),
    path("groups", GetGroups.as_view()),
    path("sport_zones", GetFlatSportZones.as_view()),
    path("sort_sport_zones_by_accessibility", SortSportZoneByAccessibility.as_view()),
    path("sort_zone_by_list_of_sport_types", SortZonesByListOfSportTypes.as_view()),
    path("sort_zone_by_name", SortSportZoneByName.as_view()),
    path("sort_zone_by_dep_name", SortSportByDepartmentName.as_view()),
    path("sport_zone/<pk>", SportZoneDetail.as_view()),
    path("sort_zones", SortZones.as_view()),
    path("departmental_org/<pk>", DepartmentOrgDetail.as_view()),
    path("group_zones", GroupSportObject.as_view()),
    path("get_info_from_zones", GetInfoFromZones.as_view()),
    path("get_info_from_group", GetInfoFromGroup.as_view()),
    path("sport_types", SportTypes.as_view())
]
