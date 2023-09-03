import orm.init_django_orm  # noqa
from db.models import Alarm, AlarmEnd


def connect_tables():

    counter = 1

    print("Connecting Alarm DB to AlarmEnd DB via OneToOneField...")

    for alarm in Alarm.objects.all():
        curr_oblast = alarm.oblast
        curr_date = alarm.date
        alarm_end = (
            AlarmEnd.objects.filter(
                date__gt=curr_date, oblast=curr_oblast, alarm__isnull=True
            )
            .order_by("date")
            .first()
        )

        if alarm_end is None:
            pass
        elif alarm_end.alarm is not None:
            pass
        else:
            alarm_end.alarm = alarm
            try:
                alarm_end.save()
                counter += 1
            except Exception as e:
                print(e)
                pass

    print(f"Finished! Number of instances operated: {counter}")


if __name__ == "__main__":
    connect_tables()
