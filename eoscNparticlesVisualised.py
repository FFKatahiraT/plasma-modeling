import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

i=0
f = 0
N = 8.0
a, v,x, y = [],[],[],[]
x_m, v_m, a_m = [],[],[]
step_m=[0]
dt = 0.0001
l = 1.0
m=[]
q=1.0
steps=0
add=l/N*2
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
	x.append(i*l/N+l/2/N)
	y.append(5.0)
	a_m[i]=[a[i]]
	v_m[i]=[v[i]]
	x_m[i]=[x[i]]
	i+=1
#m[2]=10**5
x[0]=l/N


def update(data):
    points.set_ydata(5)
    points.set_xdata(data)
    return points,

def generate_points():
	global f
	global steps
	while steps<50:
		i=0
		while i < N:
			f=0
			while f < N:
				accel1 =0
				accel2 =0
				accel3 =0
				if x[i] == x[f]:
					if f+1<N:
						f+=1
					else:
						break
				if abs(x[i]-x[f]-l)<add:
					accel1 = (x[i]-x[f]-l)/abs((x[i]-x[f]-l)**3)*q**2/m[i]
					print('close to right')
				if l+x[i]-x[f]<add:
					accel2 = (l+x[i]-x[f])/abs((l+x[i]-x[f])**3)*q**2/m[i]
					print('close to left')
				if abs(x[i]-x[f])<add:
					accel3 = (x[i]-x[f])/abs((x[i]-x[f])**3)*q**2/m[i]
					#dx = (x[i]-x[f])
					#accel = find_nearest(force_m,dx)/m[i]
				a[i] = a[i] + accel1+accel2+accel3
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
			#print(a[i], x[i],steps, 'axs',i)
			a[i]=0.0
			i+=1
		steps +=1
	steps=0
        yield x# change this

fig, ax = plt.subplots()
print(x,y)
points, = ax.plot(x, 'o')
ax.set_xlim(0,l)
ax.set_ylim(0,10)
ani = animation.FuncAnimation(fig, update, generate_points, interval=20)
plt.show()

