import confiq
# eps = confiq.eps
def compute_acceleration(root,x, y):
    G = 0.03763 #Gravitational constant Unit: AU , Year, M_jupiter
    if root.children is None:
        x_g, y_g = root.center_of_mass
        r = ((x-x_g)**2 + (y-y_g)**2)**(0.5)
        if r == 0:
            return 0, 0
        else:
            F_x = G*root.mass * (x_g-x)/r**3
            F_y = G*root.mass * (y_g-y)/r**3
            return F_x, F_y
    else:
        F_x, F_y = 0, 0
        D = root.bbox[1] - root.bbox[0] #size of the node
        x_g, y_g = root.center_of_mass
        r = ((x-x_g)**2 + (y-y_g)**2)**(0.5)
        theta = D/r
        if theta <= confiq.eps:
            #condition for the approximation
            F_x += G*root.mass * (x_g-x)/r**3
            F_y += G*root.mass * (y_g-y)/r**3
            return F_x, F_y
        else:
            for child in root.children:
                if child.n == 0:
                    continue
                else:
                    a, b = compute_acceleration(child, x, y)
                    F_x += a
                    F_y += b
            return F_x, F_y
