from orm import init_django_orm  # noqa

import os
import csv
from db.models import Alarm
from db.get_alarms import get_alarms

alarms = get_alarms()

root_dir = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(root_dir, "my_csv", "hours_alarms.csv")


def get_hours_alarms_csv():
    oblasts = []
    starts = []
    ends = []
    durations = []

    for alarm in alarms:
        alarm_end = alarm.alarmend

        alarm_date = alarm.date
        alarm_end_date = alarm_end.date

        alarm_duration = alarm_end_date - alarm_date
        alarm_oblast = alarm.oblast

        print(
            f"Oblast: {alarm_oblast}. Start: {alarm_date}. End: {alarm_end_date}. Duration: {alarm_duration}."
        )

        oblasts.append(alarm_oblast)
        starts.append(alarm_date)
        ends.append(alarm_end_date)
        durations.append(alarm_duration)

    with open(
        "hours_alarms.my_csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        csvwriter = my_csv.writer(csvfile)
        csvwriter.writerow(["Oblast", "Start", "End", "Duration"])
        for oblast, start, end, duration in zip(
            oblasts, starts, ends, durations
        ):
            csvwriter.writerow([oblast, start, end, duration])
