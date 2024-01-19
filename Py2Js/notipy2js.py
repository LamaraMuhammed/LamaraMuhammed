from plyer.platforms.win.notification import balloon_tip

def send_notification():
    balloon_tip(title="from py2js", message=f"This is a message  from send_notification", app_name="utf-8")


def send_noti_arg(x):
    balloon_tip(title="from py2js", message=f"This is a message got '{x}' from send_noti_arg", app_name="utf-8")



send_notification()

send_noti_arg("NodeJs")

