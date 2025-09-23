import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)

stop= 9
GPIO.setup(stop, GPIO.IN)
light_time=0.2

while(True):
	if (GPIO.input(stop)==1):
		break;
	for leds in led:
		GPIO.output(leds, 1)
		time.sleep(light_time)
		GPIO.output(leds,0)

time.sleep(1)

while(True):
	if (GPIO.input(stop)==1):
		break
	for leds in reversed(led):
		GPIO.output(leds, 1)
		time.sleep(light_time)
		GPIO.output(leds, 0)

GPIO.output(led, 0)
