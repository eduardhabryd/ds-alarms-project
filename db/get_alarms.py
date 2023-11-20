import orm.init_django_orm  # noqa

from scrap import scrap_telegram
from db.models import Alarm


def get_alarms():
    if Alarm.objects.all().count() > 20_000:
        return Alarm.objects.filter(alarmend__isnull=False)
    else:
        print(
            "Database either not full enough for analysis "
            "or not filled with data. "
            "Trying to scrap..."
        )
        scrap_telegram.scrap()
