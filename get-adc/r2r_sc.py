import r2r_adc as r2r
import adc_plot as plt
import time

r2r=r2r.R2R_ADC(3.211)
voltage_values=[]
time_values=[]
duration =3.0

if __name__=='__main__':
    try:
        T=time.time()
        while(time.time()-T<=duration):
            voltage_values.append(r2r.sequential_counting_adc())
            time_values.append(time.time()-T)
        plt.plot_voltage_vs_time(time_values, voltage_values,3.211)
        plt.plot_sampling_hist(time_values)
    finally:
        r2r.deinit()