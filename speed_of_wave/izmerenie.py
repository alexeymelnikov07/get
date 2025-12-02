import mcp3021 as mcp
import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setmode(GPIO.BCM)

adc = mcp.MCP3021(5.18,False)
time_start=time.time()
str=0
gerk=15
GPIO.setup(gerk, GPIO.IN)
data=[]
vrem=[]
a=0
try:
    print("ждём")
    while (GPIO.input(gerk)):
        pass
    print("ПОЕХАЛИ")
    while(True):
        data.append(adc.get_number())
        vrem.append(time.time()-time_start)
        str+=1


finally: 
    with open("./izmer_100.txt", 'w') as file:
        file.write(f'Время[c],АЦП \n')
        for i in range (str):
            file.write(f'{vrem[i]}, {data[i]:.0f} \n')
    adc.deinit()