from compute_acceleration import compute_acceleration
import numpy as np
from center_of_mass import center_of_mass
from node import Node
from quad_insert import quad_insert
import confiq
def integrate(root, X0, Y0, v_x0, v_y0, mass, t_f , n_t ):
    """Input:
        root: the root node
        [x0 y0]: initial position
        [v_x0, v_y0]: initial velocity
        mass: mass of the particles
        t_f: final time
        n:  number of time step
       Output:
        x, y: position of all particle in every time step
        v_x, v_y: velocity of all particle in every time step
    """
    dt = t_f / n_t
    N = len(X0)
    x = np.zeros((N, n_t+1))
    y = np.zeros((N, n_t+1))
    v_x = np.zeros((N, n_t+1))
    v_y = np.zeros((N, n_t+1))
    a_x0 = np.zeros((N,n_t+1))
    a_y0 = np.zeros((N,n_t+1))
    x[:,0], y[:,0], v_x[:,0], v_y[:,0] = X0, Y0, v_x0, v_y0
    for i in range(N): #initial acceleration
        a_x0[i,0], a_y0[i,0] = compute_acceleration(root, X0[i], Y0[i])
    for j in range(1,n_t+1):
        root = Node((-confiq.l,confiq.l,-confiq.l,confiq.l))
        for i in range(N):
            x[i,j] = x[i,j-1] + v_x[i,j-1]*dt + 0.5*a_x0[i,j-1]*dt**2
            y[i,j] = y[i,j-1] + v_y[i,j-1]*dt + 0.5*a_y0[i,j-1]*dt**2
            quad_insert(root, x[i,j], y[i,j], mass[i])
        center_of_mass(root)
        for i in range(N):
            #current acceleration
            a_x, a_y = compute_acceleration(root, x[i,j], y[i,j])
            a_x0[i,j], a_y0[i,j] = a_x, a_y #save it for future use, a_p: previous acceleration
            v_x[i,j] = v_x[i,j-1] + 0.5*(a_x0[i,j] + a_x0[i,j-1])*dt
            v_y[i,j] = v_y[i,j-1] + 0.5*(a_y0[i,j] + a_y0[i,j-1])*dt
        # if j == 1:
        #     break
    return x, y, v_x, v_y, a_x0, a_y0
