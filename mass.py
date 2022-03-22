def mass(root):
    """ computing recursively
        the mass of each node
        inside root and itself
    """
    if root.children is None:
        return root.mass
    else:
        root.mass = 0
        for child in root.children:
            #sum of mass of all its children
            root.mass += mass(child)
        return root.mass
