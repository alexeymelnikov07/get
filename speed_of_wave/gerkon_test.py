import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gerk=15

GPIO.setup(gerk, GPIO.IN)

while(True):
    print(GPIO.input(gerk))
    time.sleep(0.1)
