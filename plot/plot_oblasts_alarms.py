import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from my_csv.get_csv_oblasts_alarms import get_oblasts_alarms_csv

root_dir = os.path.dirname(os.path.dirname(__file__))
csv_path = os.path.join(root_dir, "my_csv", "oblasts_alarms.csv")
plot_path = os.path.join(root_dir, "images/oblasts_alarms.png")


def plot():
    get_oblasts_alarms_csv()
    data = pd.read_csv(csv_path)

    data = data.sort_values(by="Alarms amount", ascending=False)

    hour = data["Oblast"]
    alarms_amount = data["Alarms amount"]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(hour, alarms_amount)
    ax.set_xlabel("Oblast")
    ax.set_ylabel("Alarms amount")
    ax.set_title("Alarms Amount Over Oblast")

    ax.set_xticklabels(hour, rotation=90)

    fig.tight_layout()

    plt.savefig(plot_path, dpi=200)


if __name__ == "__main__":
    plot()
