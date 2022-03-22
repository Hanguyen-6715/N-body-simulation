def get_particle(root):
    """ Output: Coordinates of all
        particles inside the root
        as two lists, x coord and y coord
    """
    if root.n == 1: #one particle:
        return [root.center_of_mass[0]], [root.center_of_mass[1]]
    else:
        x, y = [], []
        for child in root.children:
                if child.n == 0: #no particle
                    continue
                a, b = get_particle(child)
                x.extend(a)
                y.extend(b)
        return x, y
def get_rectangle(root):
    """ output. xy: coordinate of the bottom-left
                    corner of the rectangle
                s: size(width) of the rectangle
    """
    if root.children is None:
        return [(root.bbox[0], root.bbox[2])], [root.bbox[1] - root.bbox[0]]
    else:
        xy, s = [], []
        for child in root.children:
            # if child.n == 0:
            #     continue
            a, b = get_rectangle(child)
            xy.extend(a)
            s.extend(b)
        
        return xy, s
