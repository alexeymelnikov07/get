import numpy as np
import time

def get_sin(freq, time):
    return float((np.sin(2*3.1415*freq*time)+1)/2)

def wait_for_sampling(sampling_period):
    time.sleep(float(1/sampling_period))


def get_triangle(freq, time, amplitude):
    if (time<(1/freq)/2):
        return(amplitude*freq*time)
    if (time>=(1/freq)/2):
        return(2*amplitude-amplitude*freq*time)