import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel('time,s')
    plt.ylabel('voltage,v')
    plt.grid()
    plt.show()

def plot_sampling_hist(time):
    h=[]
    for i in range(1,len(time)):
        h.append(time[i]-time[i-1])
    plt.figure(figsize=(10,6))
    plt.hist(h)
    plt.xlim(0, 0.06)
    plt.grid()
    plt.xlabel('Период измерения,с')
    plt.ylabel('Количество измерений')
    plt.show()
