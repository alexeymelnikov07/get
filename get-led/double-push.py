import RPi.GPIO as GPIO
import time
 

GPIO.setmode(GPIO.BCM)

leds=[16,12,25,17,27,23,22,24]

GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)

up=9
down=10
GPIO.setup(up,GPIO.IN)
GPIO.setup(down,GPIO.IN)

num=0

stop=13
GPIO.setup(stop,GPIO.IN)

def dec2bin(value):
	return[int(element) for element in bin(value)[2:].zfill(8)]
def dec2bin1(value):
	return[bin(value)[2:].zfill(8)]
sleep_time=0.2

while(True):
	if GPIO.input(stop)==1:
		break
	if num>=255:
		break
	if GPIO.input(up)==1 and GPIO.input(down)==1:
		str=dec2bin(255)
		GPIO.output(leds,str)
		num=255
		time.sleep(1)
	if GPIO.input(up):
		num+=1
		print (num, dec2bin(num))
		str=dec2bin(num)
#		print(type(str))
#		bin=eval(str)
		GPIO.output(leds,str)
		time.sleep(sleep_time)
time.sleep(1)

while(True):
	if GPIO.input(stop)==1:
		break
	if num<=0:
		break
	if GPIO.input(up)==1 and GPIO.input(down)==1:
		str=dec2bin(0)
		GPIO.output(leds,str)
		num=0
		time.sleep(1)
	if GPIO.input(down):
		num-=1
		print (num, dec2bin(num))
		str=dec2bin(num)
		GPIO.output(leds,str)
		time.sleep(sleep_time)

GPIO.output(leds, 0)
