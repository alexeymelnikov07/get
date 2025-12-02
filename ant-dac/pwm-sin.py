import pwm_dac as pwm
import signal_generator as sg
import time

amplitude=3.162
signal_freq=10
sampling_freq=1000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12,500,3.162,True)
        T=time.time()
        while True:
            try:
                t=time.time()-T
                voltage=sg.get_sin(signal_freq,t)*amplitude
                dac.set_voltage(voltage)
                sg.wait_for_sampling(sampling_freq)

            except ValueError:
                print("Вы ввели не число.\n")

            finally:
                f=False

    finally:
        dac.deinit()