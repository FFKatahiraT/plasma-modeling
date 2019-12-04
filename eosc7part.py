import numpy as np
import matplotlib.pyplot as plt

def func (x_i, q, l, m):
	a = (q**2.0*((x_i[i] - x_i[i+1])/abs((x_i[i] - x_i[i+1])**3.0)+(x_i[i] - x_i[i+2])/abs((x_i[i] - x_i[i+2])**3.0)+(x_i[i] - x_i[i+3])/abs((x_i[i] - x_i[i+3])**3.0)+(x_i[i] - x_i[i+4])/abs((x_i[i] - x_i[i+4])**3.0)+(x_i[i] - x_i[i+5])/abs((x_i[i] - x_i[i+5])**3.0)+(x_i[i] - x_i[i+6])/abs((x_i[i] - x_i[i+6])**3.0))/m)	#*2.5318681318681316e+22
	return a

l = 1.0 #*10**-10
m=1.0	#electron mass
q=1.0	#electron charge
step = 0
x_i = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#x_1 = 0.6
#x_2 = 0.1
v_i = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#v_1 = 0.0
#v_2 = 0.0
a_i = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
#a_1 = 0.0
#a_2 = 0.0

a_i_m = [[], [], [], [], [], [], []]
v_i_m = [[], [], [], [], [], [], []]
x_i_m = [[], [], [], [], [], [], []]
step_m = []
dt =0.00001	#6.289674077406555e-17
while step < 40000:
	i=0
	while i < 7:
		if x_i[i] > l :
			x_i[i] = x_i[i] - l
		elif x_i[i] < 0:
			x_i[i] = l + x_i[i]
		if i==1:
			x_i[i+6] = x_i[0]
		elif i==2:
			x_i[i+6] = x_i[1]
			x_i[i+5] = x_i[0]
		elif i == 3:
			x_i[i+6] = x_i[2]
			x_i[i+5] = x_i[1]
			x_i[i+4] = x_i[0]
		elif i == 4:
			x_i[i+6] = x_i[3]
			x_i[i+5] = x_i[2]
			x_i[i+4] = x_i[1]
			x_i[i+3] = x_i[0]
		elif i == 5:
			x_i[i+6] = x_i[4]
			x_i[i+5] = x_i[3]
			x_i[i+4] = x_i[2]
			x_i[i+3] = x_i[1]
			x_i[i+2] = x_i[0]
		elif i == 6:
			x_i[i+6] = x_i[5]
			x_i[i+5] = x_i[4]
			x_i[i+4] = x_i[3]
			x_i[i+3] = x_i[2]
			x_i[i+2] = x_i[1]
			x_i[i+1] = x_i[0]
		a_i[i] = (func(x_i, q, l, m))
		#print(a_i[0], 'a_1')
		v_i[i] = (v_i[i] + a_i[i]*dt)	#1589907.5018722333
		x_i[i] = (x_i[i]+v_i[i]*dt+a_i[i]*dt**2/2)
		v_i_m[i].append(v_i[i])
		x_i_m[i].append(x_i[i])
		a_i_m[i].append(a_i[i])
		i +=1
	step_m.append(step)
	step += 1
		
		
print(x_i_m[0], 'x')
print(step_m, 'steps')
plt.plot(step_m, x_i_m[0], label='x_1 [10**-10 m]')
plt.plot(step_m, x_i_m[1], label='x_2')
plt.plot(step_m, x_i_m[2], label='x_3')
plt.plot(step_m, x_i_m[3], label='x_4')
plt.plot(step_m, x_i_m[4], label='x_5')
plt.plot(step_m, x_i_m[5], label='x_6')
plt.plot(step_m, x_i_m[6], label='x_7')
plt.legend(loc='best')
plt.xlabel('steps')
plt.ylabel('x (t)')
plt.grid()
plt.show()