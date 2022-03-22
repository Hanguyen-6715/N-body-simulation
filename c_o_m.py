def c_o_m(root, x, y, m):
    """ changing the center_of_mass
        of the root due to the
        additional particle
    """
    x_root, y_root = root.center_of_mass
    x_g = (x_root*root.mass + x*m) / (root.mass+m)
    y_g = (y_root*root.mass + y*m) / (root.mass+m)
    root.center_of_mass = [x_g, y_g]
