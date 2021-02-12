from plyer import notification

def notify(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 5
    )

if __name__ == '__main__':
    notify("sankalp","hello")