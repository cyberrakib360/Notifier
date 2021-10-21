import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Learn python",
            message = "Learn python to light up your future",
            app_icon = "icon.ico",
            timeout=10
        )
        time.sleep(60*60)