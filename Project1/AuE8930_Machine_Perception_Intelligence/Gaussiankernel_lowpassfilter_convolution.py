from pylab import *
import numpy as np
from numpy import pi,exp
import matplotlib.pyplot as plt
x_new=[]
variance=1
MU=0
SD=np.sqrt(variance)
var=np.arange(500)
for u in range(len(var)):
  x_new.append(20)
s = np.random.normal(MU, SD, 500)
sig=x_new+s
figure, axis = plt.subplots(3, 1)

plt.subplots_adjust(hspace=2)
axis[0].set_title('Signal with noise and without noise')
axis[0].plot(var,sig,var,x_new)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

def gaussian_conv(A,B):
  len1=np.size(A)
  len2=np.size(B)
  value = np.zeros(len1 + len2 -1)
  for v in np.arange(len1):
    for w in np.arange(len2):
      value[v+w] = value[v+w] + A[v]*B[w]
  return value

window_3=[0.27901,0.44198,0.27901]

conv_func=gaussian_conv(sig,window_3)
len_conv=len(conv_func)-1
conv_func=conv_func[1:len_conv]

axis[1].set_title('Gaussian Kernel window size 3- filter')
axis[1].plot(var,conv_func,var,x_new)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

window_11=[0.000003,0.000229,0.005977,0.060598,0.24173,0.382925,0.24173,0.060598,0.005977,0.000229,0.000003]

conv_func1=gaussian_conv(sig,window_11)
len_conv=len(conv_func1)-5
conv_func1=conv_func1[5:len_conv]

axis[2].set_title('Gaussian Kernel window size 11- filter')
axis[2].plot(var,conv_func1,var,x_new)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
plt.show()
