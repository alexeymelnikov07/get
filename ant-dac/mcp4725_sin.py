import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude=5.23
signal_freq=10
sampling_freq=1000

if __name__=="__main__":
    try:
        func = mcp.MCP4725(5.23)
        T=time.time()
        while True:
            try:
                t=time.time()-T
                voltage=sg.get_sin(signal_freq, t)*amplitude
                voltage=func.set_voltage(voltage)
                func.set_number(voltage)
                sg.wait_for_sampling(sampling_freq)

            except ValueError:
                print("Вы ввели не число.")        
            finally:
                f=False

    finally:
        func.deinit()