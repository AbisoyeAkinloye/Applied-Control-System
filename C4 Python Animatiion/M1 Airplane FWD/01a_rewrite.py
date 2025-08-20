import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation

# simulation parameter
t0 = 0              # initial time in hrs
tf = 2              # final time in hrs
dt = 0.005          # time step
t = np.arange(t0, tf+dt, dt)    # time vector
frames = len(t)

# parameter
x = 800*t           # distance in km
altitude = 2
y = np.ones(len(t))*altitude

# figure
fig = plt.figure(figsize=(16,9), dpi=120, facecolor=[0.8, 0.8, 0.8])
gs = GridSpec(2,2)
ax = fig.add_subplot(gs[0,:], facecolor=[0.9, 0.9, 0.9])
ax.set_xlim(min(x),max(x))
ax.set_ylim(0,3)


# animation
animated_line, = ax.plot([],[],'r',linewidth=2)

def update_plot(frame):
    animated_line.set_data(x[:frame], y[:frame])
    return animated_line,

animation = FuncAnimation(fig,update_plot,frames,interval=20,repeat=True)

plt.show()
