import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
print "LED on"
GPIO.output(11,GPIO.HIGH)
time.sleep(2)
GPIO.output(11,GPIO.LOW)
