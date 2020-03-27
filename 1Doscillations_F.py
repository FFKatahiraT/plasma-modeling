#This program calculate x(t) for every particle in 1D. It saves .dump file for VMD visualisation program

import numpy as np
import matplotlib.pyplot as plt
import os

i=0
f = 0
N = 500.0	#Choose number of particles here
a, v,x, y = [],[],[],[]
x_m, v_m, a_m = [],[],[]
ReRho_list, ImRho_list=[],[]
rho_rho_list=[]
step_m=[0]
dt = 0.001	#time step for every calculation
l = 20.0	#length
m=[]
q=1.0	#charge
steps=0
add=l
temp=[0]
#gamma= 0.5	#Plasma imperfection coeffiient
k_const=6.28/l*2
#Temperature = q**2*N/(l*gamma) #31.75*10**4 K
Temperature = 10
while i<N:
	m.append(1)
	a_m.append(temp)
	v_m.append(temp)
	x_m.append(temp)	
	i+=1

av_velocity = Temperature/m[0]
i=0
while i < N:
	a.append(0.0)
	v.append(np.random.uniform(-2*av_velocity,2*av_velocity))
	x.append(i*l/N+l/2/N)
	y.append(5.0)
	a_m[i]=[a[i]]
	v_m[i]=[v[i]]
	x_m[i]=[x[i]]
	i+=1
#m[2]=10**5
#x[0]=l/N/2+0.25
print(v, 'initial velocity')

x_m[0][0]=x[0]
if os.path.exists('eoscNparticles.dump') == True:
	os.remove('eoscNparticles.dump')	
file1 = open("eoscNparticles.dump","w") 

while steps<5000:
	file1.write("ITEM: TIMESTEP\n")
	file1.write(str(steps))
	file1.write('\nITEM: NUMBER OF ATOMS\n')
	file1.write(str(N))
	file1.write('\nITEM: BOX BOUNDS pp ss ss\n0 ')
	file1.write(str(l)) 
	file1.write('\n0 ')
	file1.write(str(l/100)) 
	file1.write('\n0 ')
	file1.write(str(l/100)) 
	file1.write('\nITEM: ATOMS id type x y z\n')
	i=0
	while i < N:
		f=0
		while f < N:
			accel =0
			if x[i] == x[f]:
				#print(i, f, 'break')
				k=2
			elif abs(x[i]-x[f]-l)<add:
				#accel = (x[i]-x[f]-l)/abs((x[i]-x[f]-l)**3)*q**2/m[i]
				accel = (x[i]-x[f]-l)/abs((x[i]-x[f]-l))*q/m[i]*6.28
				#print('close to right')
			elif l+x[i]-x[f]<add:
				#accel = (l+x[i]-x[f])/abs((l+x[i]-x[f])**3)*q**2/m[i]
				accel = (l+x[i]-x[f])/abs((l+x[i]-x[f]))*q/m[i]*6.28
				#print('close to left')
			elif abs(x[i]-x[f])<add:
				#accel = (x[i]-x[f])/abs((x[i]-x[f])**3)*q**2/m[i]
				accel = (x[i]-x[f])/abs((x[i]-x[f]))*q/m[i]*6.28
			else:
				k=2
			a[i] = a[i] + accel
			f +=1
		i+=1
	ReRho=0
	ImRho=0
	i=0
	while i<N:
		v[i] = (v[i] + a[i]*dt)	#1589907.5018722333
		#print(v[i])
		x[i] = (x[i]+v[i]*dt+a[i]*dt**2/2)
		if x[i]>l/2:
			x[i]-=l
		ReRho+=np.cos(k_const*x[i])
		ImRho+=np.sin(k_const*x[i])
		if x[i] > l :
			x[i] = x[i] - l
		elif x[i] < 0:
			x[i] = l + x[i]
		#print(a[i], x[i],steps, 'axs',i)
		x_m[i].append(x[i])
		a_m[i].append(a[i])
		v_m[i].append(v[i])
		J=[str(i+1)]
		file1.writelines(J)
		file1.write(' 1 ')
		K=[(str(x[i]))]
		file1.writelines(K)
		file1.write(' ')
		file1.write(str(y[0]))
		file1.write(' 0\n')
		a[i]=0.0
		i+=1
	ReRho_list.append(ReRho)
	ImRho_list.append(ImRho)
	step_m.append(steps)
	print(steps, ' current step')
	steps+=1
file1.close() #to change file access modes 

F_distr=[]
j=0
while j<steps:
	rho_rho_list.append(ReRho_list[j]*np.cos(k_const*x[0])+ImRho_list[j]*np.sin(k_const*x[0]))
	j+=1
i=0
while i<1000:
	SUM=0
	j=0
	while j<=40:
		SUM+=rho_rho_list[j*100+i]
		j+=1
	F_distr.append(SUM/40)
	i+=1

plt.scatter(range(steps),ReRho_list)
#plt.legend(loc='best')
plt.xlabel('steps')
plt.ylabel('ReRho')
plt.title('ReRho')
plt.show()

plt.scatter(range(steps),ImRho_list)
#plt.legend(loc='best')
plt.xlabel('steps')
plt.ylabel('ImRho')
plt.title('ImRho')
plt.show()

plt.scatter(range(1000),F_distr, label=i)
#plt.legend(loc='best')
plt.xlabel('')
plt.ylabel('')
plt.title('F Distribution')
plt.show()

i=0
#print(x_m)
while i<N:
	plt.plot(step_m,x_m[i], label=i)
	#plt.legend(loc='best')
	plt.xlabel('steps')
	plt.ylabel('x (t)')
	plt.title(' X (t) plot')
	i+=1
plt.show()