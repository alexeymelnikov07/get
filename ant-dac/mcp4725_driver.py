import smbus

class MCP4725:
    def __init__(self,dynamic_range, address=0x61, verbose = True):
        self.bus=smbus.SMBus(1)

        self.address=address
        self.wm=0x00
        self.pds=0x00

        self.verbose=verbose
        self.dynamic_range=dynamic_range

    def deinit(self):
        self.bus.close()
    
    def set_number(self,number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")

        if not (0<=number<=4095):
            print("Число выходит за разрядность (12бит)")

        first_byte=self.wm | self.pds | number >>8
        second_byte=number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число : {number}, отправленны по I2C данные: [0x{(self.address<<1):02X},0x{first_byte:02X}, 0x{second_byte:02X}]\n")

    def set_voltage(self,voltage):
        if not (0.0<= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за дин. диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("устанавливаем 0.0 В")
            return 0
        return int(4095*voltage/self.dynamic_range)


if __name__=="__main__":
    try:
        func = MCP4725(5.23)

        while True:
            try:
                voltage=float(input("Введите напряжение (В): "))
                voltage=func.set_voltage(voltage)
                func.set_number(voltage)

            except ValueError:
                print("Вы ввели не число.")        
            finally:
                f=False

    finally:
        func.deinit()