import plyer

import requests

from plyer import notification

notification_title = "DRINK WATER!!"

notification_message="you must drink water now bro"

notification.notify(title=notification_title,message=notification_message,app_icon=None,timeout=10,toast=False)




