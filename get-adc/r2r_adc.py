import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self,dynamic_range,compare_time =0.0001,verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose=verbose
        self.compare_time=compare_time

        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio,GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio,0)
        GPIO.cleanup()
    
    def number(self,number):
        binary=[int(elemet) for elemet in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio,binary)
    
    def sequential_counting_adc(self):
        for i in range (256):
            self.number(i)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio):
                return i/255*self.dynamic_range
            if i==255:
                return i/255*self.dynamic_range
    
    def get_sc_voltage(self):
        print(f'Напряжение: {(self.sequential_counting_adc())}')

    def successive_approximation(self,bit):
        h=[]
        for i in range (bit):
            h.append(0)
        for i in range (bit):
            h[i]=1
            GPIO.output(self.bits_gpio,h)
            time.sleep(self.compare_time)
            if not GPIO.input(self.comp_gpio):
                continue
            else:
                h[i]=0
        res=0
        for i in range(bit):
            res+=h[i]*2**(7-i)
        return res/255*self.dynamic_range

    def get_sar_voltage(self):
        print (f'Напряжение: {self.successive_approximation(8)}')

if __name__=="__main__":
    try:
        r2r=R2R_ADC(3.221)
        while(True):
            try:
                # print('Способ 1: ')
                # r2r.get_sc_voltage()
                # print('\n')
                # print('Способ 2: ')
                r2r.get_sar_voltage()
                print('\n')
            finally:
                f=False
            # r2r.number(255)
    finally:
        r2r.deinit()








