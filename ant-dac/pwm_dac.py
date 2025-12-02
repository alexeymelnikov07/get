import RPi.GPIO as GPIO


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
            self.dynamic_range=dynamic_range
            self.gpio_pin=gpio_pin
            self.pwm_frequency=pwm_frequency
            self.verbose=verbose
            self.duty=0
            self.running=False

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_pin, GPIO.OUT)
            self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)


    def deinit(self):
        GPIO.output(self.gpio_pin,0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0<= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за дин. диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("устанавливаем 0.0 В")
            return 0
        self.duty=voltage/self.dynamic_range*100
        print(f'Коэффициент заполнения: {self.duty:.2f}')
        
        if (not self.running):
            self.pwm.start(self.duty)
        else:
            self.pwm.ChangeDutyCycle(self.duty)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12,500,3.16,True)

        while True:
            try:
                voltage=float(input("Введите напряжение (В): "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число.\n")

            finally:
                f=False

    finally:
        dac.deinit()

    

    
    