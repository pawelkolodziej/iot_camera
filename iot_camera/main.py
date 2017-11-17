import pir
from camera import Camera
import os
import time
import server
import iot_temp_humidity.sensor as sensor

def startMotionDetect():
    cam = Camera()
    while True:
        motion = pir.isMotionDetected()
        if motion==1: #PIR signal is LOW
            print "No motion"
        elif motion==0: #PIR signal is HIGH
            print "Motion"
            cam.makePreview(5)
            #os.system('bash ./pushbullet.sh "hey, its me"')
        time.sleep(1)
        
#startMotionDetect()
sensor.getTempAndHumidityFromSensor()
server.startServer()