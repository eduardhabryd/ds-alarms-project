import os
from plot.plot_all import plot_all
from scrap import scrap_telegram


def cli_should_renew_info() -> None:
    answer = input("Should we renew information about alarms? [y/n]: ").lower()
    if answer.startswith("y"):
        scrap_telegram.scrap()
        plot_all()
    else:
        pass


def check_for_plots() -> None:
    plots = [
        os.path.exists("hours_alarms.png"),
        os.path.exists("oblasts_alarms.png"),
    ]
    if all(plots):
        print(
            "All plots are presented. "
            "You can check .png files inside the root folder."
        )
    else:
        plot_all()
        print("Plots were created in the root folder!")


def main():
    check_for_plots()
    cli_should_renew_info()


if __name__ == "__main__":
    main()
