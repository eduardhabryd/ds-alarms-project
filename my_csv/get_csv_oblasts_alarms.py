from orm import init_django_orm  # noqa

import os
import csv
from db.get_alarms import get_alarms

alarms = get_alarms()

root_dir = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(root_dir, "my_csv", "oblasts_alarms.csv")


def get_oblasts_alarms_csv():
    oblasts = {
        "Запорізька": 0,
        "Донецька": 0,
        "Харківська": 0,
        "Миколаївська": 0,
        "Херсонська": 0,
        "Сумська": 0,
        "Одеська": 0,
        "Дніпропетровська": 0,
        "Полтавська": 0,
        "Тернопільська": 0,
        "Чернівецька": 0,
        "Рівненська": 0,
        "Хмельницька": 0,
        "Житомирська": 0,
        "Київська": 0,
        "Чернігівська": 0,
        "Вінницька": 0,
        "Кіровоградська": 0,
        "Черкаська": 0,
        "Волинська": 0,
        "Закарпатська": 0,
        "Івано-Франківська": 0,
        "Львівська": 0,
        "Луганська": 0,
    }
    counter = 0
    print("Generating cvs file for alarms over oblasts chart...")
    for oblast in oblasts:
        oblasts[oblast] = alarms.filter(oblast=oblast).count()
    # for alarm in alarms:
    #     oblast = alarm.oblast
    #     if oblasts.get(oblast):
    #         oblasts[oblast] += 1
    #         print(oblast[oblast])
    #     else:
    #         oblasts[oblast] = 0
    #         print(oblasts)
    #     counter += 1

    print(f"{counter} alarms were operated.")

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Oblast", "Alarms amount"])
        for oblast, alarms_amount in oblasts.items():
            csvwriter.writerow([oblast, alarms_amount])


if __name__ == "__main__":
    get_oblasts_alarms_csv()
