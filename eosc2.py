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
	dydt = [v, (q**2/((l + x)**2*m)-q**2/((l - x)**2*m))]
	return dydt

freq_m = []
y_m = []
y_mv=[]
t = np.linspace(0,500, 501)
q = float(1)
l = float(1.0)
m = float(1)
y0 = [0.1, 0]
w=[]
omega=q*np.sqrt(4/(m*l**3))
print(omega, ' Theoretical frequency')
a=0
d = 10
while a < d:
	w.append(omega)
	a += 1

while(y0[0]<l-0.05):
	y_m.append(y0[0])
	y_mv.append(y0[1])
	y = odeint(model ,y0 ,t , args=(q, l, m))
	zcr = np.where(np.diff(np.sign(y[:,0])))[0]
	T = (zcr[3]-zcr[1])
	y0[0] += 0.06
	print(y0)
	Tf = float(T)
	freq = 1/Tf*6.28
	freq_m.append(freq)
	y0[1] = q*y0[0]*np.sqrt(1/(l*(l**2-y0[0]**2)*m))

'''
freq_mv=[]
freq_mv=freq_m
approxx=np.polyfit(freq_m, y_m,1)
error = np.sum((np.polyval(np.polyfit(freq_m, y_m, 1), freq_m) - y_m)**2)
while error >1:
	del y_m[0:1]
	del freq_m[0:1]
	error = np.sum((np.polyval(np.polyfit(freq_m, y_m, 1), freq_m) - y_m)**2)

#approxv=np.polyfit(freq_mv, y_mv,1)
#print(approxx)
'''

plt.figure()
plt.subplot(211)
plt.plot(y_mv, freq_m)
plt.ylabel('frequency 3.1*10**16 Hz')
plt.xlabel('Initial velocity (3.2*10**6)')
plt.grid()

plt.subplot(212)
plt.plot(y_m, freq_m)
plt.plot(w)
plt.ylabel('frequency 3.1*10**16 Hz')
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