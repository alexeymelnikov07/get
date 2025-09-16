import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led=26
GPIO.setup(led,GPIO.OUT)
photo=6
GPIO.setup(photo,GPIO.IN)
while True:
	if (GPIO.input(photo)==1):
		GPIO.output(led,photo)
	else:
		GPIO.output(led,0)
#while True:
	#photo=not photo
	#GPIO.output(led.photo)
