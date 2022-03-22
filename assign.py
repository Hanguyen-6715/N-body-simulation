def assign(root,x,y,m):
    #assign a particle with coord [x,y] mass m
    # in a root which has no particles
    root.mass += m
    root.center_of_mass = [x,y]
    root.n += 1
    return root
