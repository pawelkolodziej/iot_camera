import time
import picamera
import datetime
import os

fileName = None

def removeoldpics():
    os.remove(fileName)

def getFileName():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")

def makePreview(lengthInSec):
    fileName = getFileName()
    cam = picamera.PiCamera()
    #cam.start_preview()
    cam.capture(fileName)
    #cam.stop_preview()
