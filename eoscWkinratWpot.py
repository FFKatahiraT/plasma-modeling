import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y,t, q, l, m):
	x, v = y
	dydt = [v, 9*(q**2/((l + x)**2*m)-q**2/((l - x)**2*m))]
	return dydt

freq_m = []
y_m = []
y_mv=[]
Wspec=[]
t = np.linspace(0,500, 501)
q = 1.6
l = 10
m = 9.3
y0 = [0.1, 0]

while(y0[0]<l-0.5):
	y_m.append(y0[0])
	y_mv.append(y0[1])
	y = odeint(model ,y0 ,t , args=(q, l, m))
	zcr = np.where(np.diff(np.sign(y[:,0])))[0]
	T = (zcr[3]-zcr[1])
	y0[0] += 0.5
	print(y0)
	Tf = float(T)
	freq = 1/Tf
	freq_m.append(freq*6.28)
	y0[1] = q*y0[0]*np.sqrt(1/(l*(l**2-y0[0]**2)*m))
	Temp=m*(y0[1])**2*2.47
	Energy=1.29*Temp
	Wspecial=9*q**2/l/Energy
	Wspec.append(Wspecial)
	

plt.plot(Wspec, freq_m)
plt.xlabel('Wpot/Wkin')
plt.ylabel('frequency 10**16 Rad/s')
plt.grid()
#plt.ylabel('y(t)')
plt.show()