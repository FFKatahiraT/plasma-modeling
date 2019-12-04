import numpy as np
import matplotlib.pyplot as plt

def func_1 (x_1, x_2, q, l, m):
	a_1 = np.float64(q**2.0*(1.0/(x_1**2.0)-1.0/(x_2 - x_1)**2.0-1.0/(l-x_1)**2.0)/m)
	return a_1

def func_2 (x_1, x_2, q, l, m):
	a_2 = np.float64(q**2.0*(1.0/(x_2**2.0)+1.0/(x_2 - x_1)**2.0-1.0/(l-x_2)**2.0)/(m))
	return a_2

q = 1.0
l = 1.0
m = 1.0
dl = 0.05
#l_1 = 0.5*(np.sqrt(31+22*np.sqrt(2.0))*l-3*np.sqrt(2.0)*l-3*l)
x_1 = 0.31926*l+dl
#x_1= 0.25*l +dl
x_2 = 0.68074*l
#x_2 = 0.5*l
print(x_1, 'l_1')
step = 0.0 
v_1 = 0.0
v_2 = 0.0
x_1_m = []
x_2_m = []
v_1_m = []
v_2_m = []
step_m = []
a_1_m = []
a_2_m = []
dt =0.0001
summ= []

while step < 50000:
	x_1_m.append(x_1)
	x_2_m.append(x_2)
	v_1_m.append(v_1)
	v_2_m.append(v_2)
	step_m.append(step)
	a_1 = np.float64(func_1(x_1, x_2, q, l, m))
	a_2 = np.float64(func_2(x_1, x_2, q, l, m))
	v_1 = np.float64(v_1 + a_1*dt)
	x_1 = np.float64(x_1+v_1*dt+a_1*dt**2/2)
	v_2 = np.float64(v_2 + a_2*dt)
	x_2 = np.float64(x_2+v_2*dt+a_2*dt**2/2)
	sumem = x_1+x_2
	summ.append(sumem)
	a_1_m.append(a_1)
	a_2_m.append(a_2)
	step += 1


print(a_1_m, ' a_1;', a_2_m, ' a_2')
print(x_1_m, ' x_1;', x_2_m, ' x_2')
plt.plot(step_m, x_1_m, label='x_1')
plt.plot(step_m, x_2_m, label='x_2')
plt.plot(step_m, summ, label='summ')
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('x (t)')
plt.grid()
plt.show()
