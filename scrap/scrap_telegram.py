import orm.init_django_orm  # noqa
import os
import asyncio
from pyrogram import Client
from dotenv import load_dotenv
from db.models import Alarm, AlarmEnd
from db.connect_tables import connect_tables
from asgiref.sync import sync_to_async

load_dotenv()


def remove_old_cvs():
    root_folder = os.path.dirname(os.path.dirname(__file__))
    folder_path = os.path.join(root_folder, "my_csv")
    files = os.listdir(folder_path)
    print("Deleting old .csv files...")
    for file in files:
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            os.remove(file_path)
            print(f"Deleted: {file_path}")


try:
    CONFIG = {
        "telegram_api_id": int(os.getenv("TG_API_ID")),
        "telegram_hash": os.getenv("TG_API_HASH"),
    }
except Exception:
    raise Exception(
        "There is no Telegram API ID or API HASH. "
        "Please add them to scrap/.env file"
        "using the following format: \n"
        "TG_API_ID='your_api_id'"
        "TG_API_HASH='your_api_hash'"
        "\nYou can get your API ID and API hash "
        "by creating a Telegram application "
        "on the Telegram Developer: "
        "https://my.telegram.org/auth?to=apps website"
    )

app = Client("my_account", CONFIG["telegram_api_id"], CONFIG["telegram_hash"])

chat_id = "air_alert_ua"


@sync_to_async
def create_alarm(date, oblast):
    if Alarm.objects.filter(date=date, oblast=oblast).exists():
        pass
    else:
        Alarm.objects.create(date=date, oblast=oblast)


@sync_to_async
def create_alarm_end(date, oblast):
    if AlarmEnd.objects.filter(date=date, oblast=oblast).exists():
        pass
    else:
        AlarmEnd.objects.create(date=date, oblast=oblast)


async def main():
    async with app:
        async for message in app.get_chat_history(chat_id):
            if message.text is None:
                print(
                    "--------------END OF SCRAPING--------------"
                )
                pass
            else:
                message_list = message.text.split()
                message_type = " ".join(message_list[2:4])
                oblast = message_list[5]
                if message_type == "Повітряна тривога":
                    await create_alarm(message.date, oblast)
                    print(message_type)
                    print(oblast)
                    print(message.date)
                    print("============================")
                if message_type == "Відбій тривоги":
                    await create_alarm_end(
                        message.date, oblast
                    )
                    print(message_type)
                    print(oblast)
                    print(message.date)
                    print("============================")


def scrap():
    remove_old_cvs()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    connect_tables()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
