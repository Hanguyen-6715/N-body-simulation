import matplotlib.pyplot as plt
import matplotlib.patches as patches
from get import get_particle, get_rectangle

def display(root):
    x, y = get_particle(root)
    xy, s = get_rectangle(root)
    fig = plt.figure(1)
    sub = fig.add_subplot(111, aspect ='equal')

    for i in range(len(s)):
        rectangle = patches.Rectangle(xy[i], s[i], s[i], fill = False)
        sub.add_patch(rectangle)
    plt.plot(x, y,'*')
    fig.show()

if __name__ == '__main__':
    from node import Node
    from quad_insert import quad_insert
    import random
    root = Node((0,1,0,1))
    N = 100 # number of particles
    for i in range(N):
        quad_insert(root, random.random(), random.random(), random.random())
    display(root)
