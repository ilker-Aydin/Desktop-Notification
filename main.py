import plyer

import requests

from plyer import notification

notification_title = "DRINK WATER!!"

message =input("notification message: ")

notification_message= message

notification.notify(title=notification_title,message=notification_message,app_icon=None,timeout=10,toast=False)




