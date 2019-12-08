import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#import glob, os
#import pandas as pd
'''
csv_file = 'eosc1.csv'
df = pd.read_csv(csv_file, index_col='Date', parse_dates=True)
os.chdir(".")
for file in glob.glob("*.csv"):
    csv_file = file.split('.csv')[0]
'''
def model(y,t, q, l, m):
	x, v = y
	dydt = [v, 9*(q**2/((l + x)**2*m)-q**2/((l - x)**2*m))]
	return dydt

freq_m = []
y_m = []
y_mv=[]
TempM=[]
EnergyM=[]
t = np.linspace(0,500, 501)
q = 1.6
l = 10
m = 9.3
y0 = [0.1, 0]
w=[]
omega=3*q*np.sqrt(4/(m*l**3))
print(omega, ' Theoretical frequency')
a=0
d = 10
while a < d:
	w.append(omega)
	a += 1

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
	TempM.append(Temp)
	EnergyM.append(Energy)

plt.figure()
plt.subplot(211)
#plt.plot(y_mv, freq_m)
plt.ylabel('frequency MHz')
plt.plot(TempM, freq_m, label='Temperature (10000 K)')
plt.plot(EnergyM, freq_m, label='Energy of a patricle (eV)')
plt.legend(loc='best')
plt.grid()

plt.subplot(212)
plt.plot(y_m, freq_m)
plt.plot(w)
plt.ylabel('frequency 10**16 Hz')
plt.xlabel('displasement amplitude (A)')
plt.grid()
plt.show()

'''
print(y_m, ' y_m')
print(freq_m, 'freq_m')
plt.plot(freq_m,y_m)
plt.plot(freq_m, approxx)
plt.xlabel('frequency')
plt.ylabel('displasement amplitude')
plt.grid()
#plt.ylabel('y(t)')
plt.show()
#plt.savefig(csv_file.split('.csv')[0])
'''