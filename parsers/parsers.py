import csv
from person_density.models import MoscowDistrict
from sport_objects.models import Accessibility, DepartmentalOrganisation, SportType, SportZone


def load_accessibility():
    Accessibility.objects.all().delete()
    Accessibility.objects.create(name="Шаговая доступность", distance=500)
    Accessibility.objects.create(name="Районное", distance=1000)
    Accessibility.objects.create(name="Окружное", distance=3000)
    Accessibility.objects.create(name="Городское", distance=5000)


def parse_sport_data():
    DepartmentalOrganisation.objects.all().delete()
    SportType.objects.all().delete()
    SportZone.objects.all().delete()
    with open("parsers/objects-with-sport-zones.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        cnt = 0
        for row in reader:
            cnt += 1
            print(row, cnt)
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
                sport_zone = SportZone.objects.get(name=row["Объект"])
                sport_zone.sport_types.add(sportType)
            except:
                SportZone.objects.create(organization=org,
                                         accessibility=Accessibility.objects.get(name=row["Доступность"]),
                                         )


def parse_person_density_data():
    with open("parsers/person_density.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            if not isinstance(row["Население"], int): continue
            MoscowDistrict.objects.create(name=row["Район"], density=row["Население"])


load_accessibility()
parse_person_density_data()
parse_sport_data()
