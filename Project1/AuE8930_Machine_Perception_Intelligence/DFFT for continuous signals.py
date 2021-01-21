import numpy as np
import matplotlib.pyplot as plotter

samplingFrequency   = 1000;
samplingInterval = 1 / samplingFrequency;

time = np.linspace(0,2, 2*samplingFrequency, endpoint = False)
amplitude1 = (3* np.cos(500 * np.pi * time)) + (2 * np.cos(1000 * np.pi * time)) + (3 * np.sin(2000 *np.pi *time)) + 2
figure, axis = plotter.subplots(2, 1)

plotter.subplots_adjust(hspace=3)

amplitude = amplitude1

axis[0].set_title('Continuous time period signal x(t)')
axis[0].plot(time[0:1000], amplitude[0:1000])
axis[0].set_xlabel('Time(microseconds)')
axis[0].set_ylabel('Amplitude')

fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

axis[1].set_title('Fourier transform depicting the frequency components')
axis[1].plot(frequencies, abs(fourierTransform))
axis[1].set_xlabel('Frequency(Hz)')
axis[1].set_ylabel('Amplitude')

plotter.show()
