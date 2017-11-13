from pushbullet import PushBullet

PUSHBULLET_API_KEY = ""
p = PushBullet(PUSHBULLET_API_KEY)
devices = p.getDevices()

def sendPushNotificationWithFile(file):
    p.pushFile(devices[0]["iden"], "Intruder Alert!", "Image From PiCam", open(file, "rb"))