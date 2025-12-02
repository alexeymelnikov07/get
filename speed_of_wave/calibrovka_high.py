import mcp3021 as mcp
import RPi.GPIO as GPIO
import time
import numpy as np

adc = mcp.MCP3021(5.18,False)
time_start=time.time()
str=1000
data=np.zeros((str,2))

try:
    for i in range (str):
        data[i,0]=adc.get_number()
        data[i,1]=time.time()-time_start

    with open("./calib_high_100.txt", 'w') as file:
        file.write(f'Время[c],АЦП \n')
        for i in range (str):
            file.write(f'{data[i,1]}, {data[i,0]:.0f} \n')

finally: 
    adc.deinit()