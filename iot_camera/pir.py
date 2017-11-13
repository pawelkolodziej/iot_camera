import RPi.GPIO as GPIO

prevState = False
currState = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #input signal from PIR sensor /PUD_DOWN?

while True:
       i=GPIO.input(11)
       if i==0:                 #PIR signal is LOW
             print "No motion",i

       elif i==1:               #PIR signal is HIGH
             print "Motion!",i

        time.sleep(1)