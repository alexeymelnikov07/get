import time
import signal_generator as sg
import r2r_dac as r2r

amplitude=3.162
signal_freq=10
sampling_freq=1000

if __name__=="__main__":
    try:
        dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22], 3.162, True)
        T=time.time()
        while True:
            try:
                t=time.time()-T
                voltage=sg.get_triangle(signal_freq,t,amplitude)
                number=dac.set_voltage(voltage)
                dac.set_number(number)
                sg.wait_for_sampling(sampling_freq)
                if (t>2*1/signal_freq):
                    T=time.time()

             #except ValueError:
                #print("Вы ввели не число.\n")

            finally:
                print()

    finally:
        dac.deinit()