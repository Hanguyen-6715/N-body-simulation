import matplotlib.pyplot as plt
import matplotlib.animation as animation
import confiq
import numpy as np
def animate(x, y):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, xlim=(-confiq.l,confiq.l), ylim=(-confiq.l,confiq.l))
    ax.set_xlabel('AU')
    ax.set_ylabel('AU')
    line, = ax.plot([],[],'*')
    time_text = ax.text(0.1, 0.9, '', transform=ax.transAxes)

    # def init():
    #     line.set_data([],[])
    #     return line,
    N, n_t = x.shape # N:number of particle, n_t: number of time point
    time_template = 'Time: {:.2f} years'
    def gen():
        for i in range(n_t):
            yield i

    def ani(i):
        a, b = np.zeros(N), np.zeros(N)
        for j in range(N):
            a[j] = x[j, i]
            b[j] = y[j, i]
        line.set_data(a, b)
        time_text.set_text(time_template.format(confiq.t[i]))
        return line, time_text
    a = animation.FuncAnimation(fig, ani, frames=n_t,
     							blit=True, repeat=True, interval=10)
    return a
