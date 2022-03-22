def center_of_mass(root):
    """calculating recursively
        the center of mass
        of each node inside the root
        and itself
    """
    from mass import mass
    if root.children is None:
        return root.center_of_mass
    else:
        x_g, y_g = 0, 0
        for child in root.children:
            x_g += center_of_mass(child)[0]*mass(child) / mass(root)
            y_g += center_of_mass(child)[1]*mass(child) / mass(root)
        return [x_g, y_g]
