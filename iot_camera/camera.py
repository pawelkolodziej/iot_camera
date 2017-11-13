import time
import picamera
import datetime
import os
import iot_camera.pushbullet as pushbullet

filename = None

def removeoldpics():
    os.remove(fileName)

def getFileName():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

cam = picamera.PiCamera()

def makePreview(lengthInSec):
    fileName = getFileName()
    cam.start_preview()
    cam.capture(fileName)
    pushbullet.sendPushNotificationWithFile(fileName)
    cam.stop_preview()
