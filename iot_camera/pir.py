import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #input signal from PIR sensor /PUD_DOWN?

def isMotionDetected():
    i = GPIO.input(11)
    return i
