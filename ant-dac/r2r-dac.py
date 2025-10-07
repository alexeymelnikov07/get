import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range,verbose=False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits,GPIO.OUT,initial=0)
    
    def deinit(self):
        GPIO.output(self.gpio_bits,0)
        GPIO.cleanup()
    
    def set_number(self, voltage):
        if not (0.0<= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за дин. диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("устанавливаем 0.0 В")
            return 0
        return int(voltage/self.dynamic_range * 255)

    def set_voltage(self, number):
        binar=[int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits,binar)

if __name__=="__main__":
    try:
        dac = R2R_DAC([16,20,21,25,26,17,27,22], 3.162, True)

        while True:
            try:
                voltage=float(input("Введите напряже(В): "))
                number=dac.set_number(voltage)
                dac.set_voltage(number)

             #except ValueError:
                #print("Вы ввели не число.\n")

            finally:
                print()

    finally:
        dac.deinit()