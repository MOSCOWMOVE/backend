from sport_objects.models import SportZone, OpenedType


def get_stats_from_ids(ids: [str]):
    points = SportZone.objects.filter(zone_id__in=ids)
    sport_types = set()
    square = 0
    polls = 0
    opened = 0
    closed = 0
    for point in points:
        sport_types.update(list(map(lambda x: x.name, point.sportTypes.all())))
        square += point.square
        if point.open_type == OpenedType.objects.get(name="Бассейн"):
            polls += 1
        elif point.open_type == OpenedType.objects.get(name="Открытое"):
            opened += 1
        else:
            closed += 1
    return {
                "sportTypes": sport_types,
                "square": square,
                "polls": polls,
                "opened": opened,
                "closed": closed
            }