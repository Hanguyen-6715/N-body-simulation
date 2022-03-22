def quad_insert(root, x, y, m):
    from assign import assign
    from check import check
    from c_o_m import c_o_m
    if root.n > 1:
        new_root = check(root,x,y)
        c_o_m(root, x, y, m)
        root.n += 1
        root.mass += m
        return quad_insert(new_root, x, y, m)
    elif root.n == 1:
        #root.center_of_mass of the parent box
        root.add_children()
        #old particle already inside the box
        x_g, y_g = root.center_of_mass
        box1 = check(root, x_g, y_g) #children box containing old particle
        assign(box1, x_g, y_g, root.mass)
        #modify the parent box
        c_o_m(root, x, y, m)
        root.mass += m
        root.n += 1
        box2 = check(root, x, y) #children box containing new particle
        return quad_insert(box2, x, y, m)
    elif root.n == 0:
        assign(root, x, y, m)
