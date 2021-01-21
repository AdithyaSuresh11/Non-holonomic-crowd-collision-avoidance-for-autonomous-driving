import numpy as np
import matplotlib.pyplot as plotter
import math

samplingFrequency = 1*10**3
time=np.linspace(0,2,samplingFrequency)
x_axis = []
time_len = np.arange(0,1000,1)
initial=0

while(initial<=((len(time_len)/2)-1)):
  x_axis.append(0)
  initial=initial+1
initial=0
while(initial<=((len(time_len)/2)-1)):
  x_axis.append(1)
  initial=initial+1
figure, axis = plotter.subplots(2, 1)

plotter.subplots_adjust(hspace=3)
axis[0].set_title('Continuous time period signal x(t)')
axis[0].plot(time_len,x_axis[0:len(x_axis)])
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

fourierTransform = np.fft.fft(x_axis)/len(x_axis)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(x_axis)/2))] # Exclude sampling frequency

tpCount     = len(x_axis)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency (Hz)')
axis[1].set_ylabel('Amplitude')

plotter.show()
