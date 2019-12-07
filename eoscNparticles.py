import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


i=0
f = 0
N = 10
a, v,x = [],[],[]
x_m, v_m, a_m = [],[],[]
step_m=[0]
dt = 0.01
l = 10.0
m=[]
q=1.0
steps=0
temp=[0]
while i<N:
	m.append(1)
	a_m.append(temp)
	v_m.append(temp)
	x_m.append(temp)	
	i+=1
i=0
while i < N:
	a.append(0.0)
	v.append(0.0)
	x.append((i+1)*l/(N+1))
	a_m[i]=[a[i]]
	v_m[i]=[v[i]]
	x_m[i]=[x[i]]
	i+=1
print(m)
#m[2]=10**5
#x[0]=0.0
x_m[0]=[x[0]]
print(x)
#print(a_m)
'''
fig = plt.figure()
ax = plt.axes()
line, = ax.plot([], [])
def init():
    line.set_data([], [])
    return line,
'''
#def animate(i):
while steps <500:
	i=0
	#global f
	step_m.append(steps)
	while i < N:
		f=0
		while f < N:
			if x[i] == x[f]:
				#print(i, f, 'break')
				k=2
			else:
				accel = (x[i]-x[f])/abs((x[i]-x[f])**3)*q**2/m[i]
				a[i] = a[i] + accel
			f +=1
		i+=1
	i=0
	while i<N:
		v[i] = (v[i] + a[i]*dt)	#1589907.5018722333
		#print(v[i])
		x[i] = (x[i]+v[i]*dt+a[i]*dt**2/2)
		if x[i] > l :
			x[i] = x[i] - l
		elif x[i] < 0:
			x[i] = l + x[i]
		print(a[i], x[i],steps, 'axs',i)
		a_m[i].append(a[i])
		v_m[i].append(v[i])
		x_m[i].append(x[i])
		a[i]=0.0
		i+=1
	#y=linspace(0,1,2)
	#line.set_data(x[0], y)
	#return line,
	steps +=1
i=0
#print(x_m[0], 'x_m')
#print(step_m, 'step_m')
while i<N:
	plt.plot(step_m, x_m[i], label='x')
	i+=1
#anim = animation.FuncAnimation(fig, animate, init_func=init,interval=200)
plt.show()