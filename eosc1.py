import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy.fftpack as spfft

def model(y,t, q, l, m):
	x, v = y
	dydt = [v, (q**2/((l + x)**2*m)-q**2/((l - x)**2*m))*2.48] #2.56*10**-38/9.3/10**-31/10**-20*10**9*9=2.48*10**22 --> 2.48*10**32
	return dydt

y0 = [0.1, 0] 	#Initial values [Displacement, velocity]
q = 1	#Charge in e (1.6*10**-19)
l = 1	#Distance between particles (A)
m = 1	#e mass (9.3*10**-31)
'''
t = np.linspace(0, 5, 501)	#init time
while y0[0]<l:
	y = odeint(model ,y0 ,t , args=(q, l, m))	#Solving ODE
	zcr = np.where(np.diff(np.sign(y[:,0])))[0]	#Finding zero crossings
	T = (zcr[2]-zcr[0])	#Calculation of period
	Tf=float(T)/100	#/100, because each point is 0.01 of time (15)
	print(Tf, 'Period 0.0001 ps')
	freq=1/Tf*6.28	#calculating frequency

	i = 1
	i += 1
	print(freq, 'frequency 10**16 rad/s')
	plt.figure(i)
	plt.plot(t, y[:, 0])
	plt.ylabel('Displacement amplitude')
	plt.xlabel('time (0.0001 ps)')
	plt.grid()
	y0[0] += 0.22
plt.show()
'''
t = np.linspace(0, 5000, 5001)	#init time
y = odeint(model ,y0 ,t , args=(q, l, m))	#Solving ODE
zcr = np.where(np.diff(np.sign(y[:,0])))[0]	#Finding zero crossings
T = (zcr[2]-zcr[0])	#Calculation of period
Tf=float(T)/100	#/100, because each point is 0.01 of time (15)
print(Tf, 'Period 0.0001 ps')
freq=1/Tf*6.28	#calculating frequency
print(freq, 'frequency 10**16 rad/s')

plt.plot(t, y[:, 0])
plt.ylabel('Displacement amplitude')
plt.xlabel('time (0.0001 ps)')
plt.grid()
plt.show()