import csv
from person_density.models import MoscowDistrict
from sport_objects.models import Accessibility, DepartmentalOrganisation, SportType, SportZone, Position, OpenedType


def load_accessibility():
    Accessibility.objects.all().delete()
    Accessibility.objects.create(name="Шаговая доступность", distance=500)
    Accessibility.objects.create(name="Районное", distance=1000)
    Accessibility.objects.create(name="Окружное", distance=3000)
    Accessibility.objects.create(name="Городское", distance=5000)


def load_opened_types():
    OpenedType.objects.all().delete()
    OpenedType.objects.create(name="Крытое")
    OpenedType.objects.create(name="Бассейн")
    OpenedType.objects.create(name="Открытое")


def get_sport_type(name: str):
    opened_type = OpenedType.objects.get(name="Открытое")
    if "крытая" in name.split() or "крытый" in name:
        opened_type = OpenedType.objects.get(name="Крытое")
    if "бассейн" in name.split():
        opened_type = OpenedType.objects.get(name="Бассейн")
    return opened_type


def parse_sport_data():
    DepartmentalOrganisation.objects.all().delete()
    SportType.objects.all().delete()
    SportZone.objects.all().delete()
    with open("parsers/objects-with-sport-zones.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        cnt = 0
        for row in reader:
            cnt += 1
            print(cnt)
            org = None
            try:
                org = DepartmentalOrganisation.objects.get(dep_id=row["id Ведомственной Организации"])
            except:
                org = DepartmentalOrganisation.objects.create(name=row["Ведомственная Организация"],
                                                              dep_id=row["id Ведомственной Организации"])

            sportType = None
            try:
                sportType = SportType.objects.get(name=row["Вид спорта"])
            except Exception:
                sportType = SportType.objects.create(name=row["Вид спорта"])

            try:
                sport_zone = SportZone.objects.get(zone_id=row["id Объекта"])
                sport_zone.sportTypes.add(sportType)
                sport_zone.open_type.add(get_sport_type(row["Тип спортзоны"]))
            except:
                opened_type = get_sport_type(row["Тип спортзоны"])
                square = row["Площадь спортзоны"]
                if len(str(row["Площадь спортзоны"])) == 0:
                    square = 0
                zone = SportZone.objects.create(organization=org,
                                                accessibility=Accessibility.objects.get(name=row["Доступность"]),
                                                name=row["Объект"],
                                                zone_id=row["id Объекта"],
                                                square=square,
                                                address=row["Адрес"]
                                                )
                zone.sportTypes.set([sportType])
                zone.open_type.set([opened_type])


def parse_person_density_data():
    MoscowDistrict.objects.all().delete()
    with open("parsers/person_density.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            if len(row["Население"]) == 0: continue
            a = MoscowDistrict.objects.create(name=row["Район"], density=float(row["Население"]))
            print(a)


def parse_lat_long_data():
    with open("parsers/lat_long_data.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id Объекта"])
            try:
                zone = SportZone.objects.get(zone_id=row["id Объекта"])
                zone.position = \
                    Position.objects.create(latitude=row["Широта (Latitude)"], longitude=row["Долгота (Longitude)"])
                zone.save()
            except:
                pass


'''
load_accessibility()
parse_person_density_data()
parse_sport_data()

parse_lat_long_data()'''
load_opened_types()
parse_sport_data()
