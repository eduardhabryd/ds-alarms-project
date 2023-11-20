import os.path

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from my_csv.get_csv_hours_alarms import get_hours_alarms_csv

root_dir = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(root_dir, "my_csv", "hours_alarms.csv")
plot_path = os.path.join(root_dir, "images/hours_alarms.png")


def plot():
    get_hours_alarms_csv()

    data = pd.read_csv(csv_path)

    hour = data["Hour"]
    alarms_amount = data["Alarms amount"]

    plt.figure(figsize=(10, 6))
    plt.plot(hour, alarms_amount, marker="o", linestyle="-")
    plt.xlabel("Hour")
    plt.ylabel("Alarms amount")
    plt.title("Alarms Amount Over Hours")
    plt.xticks(np.arange(0, 24))
    plt.grid(True)

    plt.savefig(plot_path, dpi=200)
