import numpy as np
import matplotlib.pyplot as plt

def func_1 (x_1, x_2, q, l, m):
	a_1 = (q**2.0*((x_1 - x_2)/abs((x_1 - x_2)**3.0))/m)	#*2.5318681318681316e+22
	return a_1

def func_2 (x_1, x_2, q, l, m):
	a_2 = (q**2.0*((x_2 - x_1)/abs((x_2 - x_1)**3.0))/m)	#*2.5318681318681316e+22
	return a_2

x_1 = 0.6
x_2 = 0.1
l = 1.0 #*10**-10
m=1.0	#electron mass
q=1.0	#electron charge
step = 0.0 
v_1 = 0.0
v_2 = 0.0
a_1 = 0.0
a_2 = 0.0

a_1_m, a_2_m = [], []
v_1_m, v_2_m = [], []
x_1_m, x_2_m = [], []
step_m = []
dt =0.0001	#6.289674077406555e-17
summ= []

while step < 10000:
	v_1_m.append(v_1)
	x_1_m.append(x_1)
	v_2_m.append(v_2)
	x_2_m.append(x_2)
	if x_1 > l :
		x_1 = x_1 - l
	elif x_1 < 0:
		x_1 = l + x_1
	if x_2 > l :
		x_2 = x_2 - l
	elif x_2 < 0:
		x_2 = l + x_2
	a_1 = (func_1(x_1, x_2, q, l, m))
	a_2 = (func_2(x_1, x_2, q, l, m))
	print (a_1, ' a_1', a_2, ' a_2')
	v_1 = (v_1 + a_1*dt)	#1589907.5018722333
	v_2 = (v_2 + a_2*dt)	#1589907.5018722333
	x_1 = (x_1+v_1*dt+a_1*dt**2/2)
	x_2 = (x_2+v_2*dt+a_2*dt**2/2)

	a_1_m.append(a_1)
	a_2_m.append(a_2)
	step_m.append(step)
	step += 1

#print(x_1_m, ' x_1')
plt.plot(step_m, x_1_m, label='x [10**-10 m]')
plt.plot(step_m, x_2_m, label='x [10**-10 m]')
plt.legend(loc='best')
plt.xlabel('steps')
plt.ylabel('x (t)')
plt.grid()
plt.show()
