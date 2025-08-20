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
plane_1, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing

def update_plot(frame):
    animated_line.set_data(x[:frame], y[:frame])
    plane_1.set_data([x[frame]-50, x[frame]+50],[y[frame]])
    fwl.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]+0.4])
    fwr.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]-0.4])
    bwl.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]+0.18])
    bwr.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]-0.18])

    return animated_line, fwl, fwr, bwl, bwr, plane_1

animation = FuncAnimation(fig,update_plot,frames,interval=20,repeat=True)

plt.show()
