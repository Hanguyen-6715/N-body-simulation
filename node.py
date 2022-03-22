class Node:
    def __init__(self, bbox, mass=0,
            center_of_mass=[0, 0],
            n=0): #number of particle inside the node
            # n is number of particle inside the box.
        self.mass = mass
        self.center_of_mass = center_of_mass
        self.bbox = bbox
       	self.children = None
        self.n = n
    def add_children(self):
        self.children = []
        x_min, x_max, y_min, y_max = self.bbox
        x_mid = (x_min + x_max)/2
        y_mid = (y_min + y_max)/2
        c1 = Node((x_mid, x_max, y_mid, y_max ) )
        self.children.append(c1)
        c2 = Node((x_min, x_mid, y_mid, y_max ) )
        self.children.append(c2)
        c3 = Node((x_min, x_mid, y_min, y_mid ) )
        self.children.append(c3)
        c4 = Node((x_mid, x_max, y_min, y_mid ) )
        self.children.append(c4)
