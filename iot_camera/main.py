import pir
import camera as cam
import os
import time
import server

def startMotionDetect(): 
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
server.startServer()