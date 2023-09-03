from orm import init_django_orm  # noqa

import os
import csv
from db.get_alarms import get_alarms

alarms = get_alarms()

root_dir = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(root_dir, "my_csv", "hours_alarms.csv")


def get_hours_alarms_csv():
    hours_alarms = {key: 0 for key in range(24)}
    counter = 0
    print("Generating cvs file for alarms over hours chart...")
    for alarm in alarms:
        alarm_hour = alarm.date.hour
        hours_alarms[alarm_hour] += 1
        counter += 1

    print(f"{counter} alarms were operated.")

    with open(
            csv_path, "w", newline="", encoding="utf-8"
    ) as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Hour", "Alarms amount"])
        for hour, alarms_amount in hours_alarms.items():
            csvwriter.writerow([hour, alarms_amount])


if __name__ == "__main__":
    get_hours_alarms_csv()
