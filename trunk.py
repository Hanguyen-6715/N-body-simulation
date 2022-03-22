from quad_insert import quad_insert
from node import Node
import numpy as np
import confiq
from integrate import integrate
from display_tree import display
import matplotlib.pyplot as plt
from animate import animate

G = 0.03763 #Gravitational constant Unit: AU , Year, M_jupiter
confiq.l = 10. #size of the box
l = confiq.l
root = Node((-l, l, -l, l))
N = 5 #number of particle:
#Sun Mercury Earth Mars Jupiter respectively
x0, y0 = [0, 0, 0, 0, 0], [0, 0.39, 1, 1.524, 5.2] #unit: AU
m = [1e3, 1.74e-4, 3e-3, 3.37e-4, 1]
v_x0 = [0, -2*np.pi*0.39/0.24, -2*np.pi, -2*np.pi*1.524/1.88, -2*np.pi*5.2/12 ]
v_y0 = [0, 0, 0, 0, 0]

for i in range(N):
    quad_insert(root, x0[i], y0[i], m[i])
# dipslay(root)

#Integrate
confiq.eps = 0.0 # approximation coefficient.
n_t = 10000 # number of time step.
t_f = 100.       #final time. unit year
confiq.dt = t_f/n_t #time step: 0.01 year
t = np.linspace(0, t_f, n_t+1)
confiq.t = t
x, y, v_x, v_y, a_x, a_y = integrate(root, x0, y0, v_x0, v_y0, m, t_f, n_t)
ani = animate(x,y)
plt.show()  
# fig3 = plt.figure(3)
# sub = fig3.add_subplot(111, xlim=(0,l), ylim=(0,l))
# plt.plot(x[1,:], y[1,:],".", x[0,:],y[0,:],".", xg,yg,'d',x[2,:],y[2,:],".", markersize = 1,)
# fig2 = plt.figure(2)
# plt.subplot(211)
# plt.plot(t, v_x[1], t, v_y[1])
# plt.subplot(212)
# plt.plot(t,(v_x[1,:]**2 + v_y[1,:]**2)*m[1])
# fig3.show()

#Total Energy
#E_p = np.zeros((n_t+1,1))
#E_c = np.zeros((n_t+1,1))
#for j in range(n_t+1):
#    for i in range(N):
#        for k in range(N):
#            if k == i :
#                continue
#            r = ((x[i,j]-x[k,j])**2 + (y[i,j] - y[k,j])**2)**(0.5) 
#            E_p[j] = E_p[j] + -G*m[i]*m[k]/r
#            
#for j in range(n_t+1):
#    for i in range(N):
#        E_c[j] = E_c[j] + 0.5*m[i]*(v_x[i,j]**2+v_y[i,j]**2)
#plt.figure()
#plt.plot(t, E_c+E_p)
#plt.xlabel('years')
#plt.ylabel(E)

#Angular momentum
#L  = np.zeros((n_t+1,1))
#for j in range(n_t+1):
#    for i in range(N):
#        L[j]  = L[j] + m[i]*(-y[i,j]*v_x[i,j] + x[i,j]*v_y[i,j])
#        
