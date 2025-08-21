import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation

# simulation parameters
t0 = 0              # initial time in hours
tf = 2              # final time in hours
dt = 0.005          # time step
t = np.arange(t0, tf+dt, dt)
frames = len(t)

# system parameter
x = 800*t          # distance travel in kilometer
altitude = 2
y = np.ones(len(t))*altitude    # altitude of the airplance

# figure and axis
fig = plt.figure(figsize=(16,9), dpi = 120, facecolor=[0.8,0.8,0.8])
gs = GridSpec(2,2)
ax = fig.add_subplot(gs[0,:],facecolor=[0.9,0.9,0.9])
ax.set_ylim(0, max(y)+1), ax.set_yticks(np.arange(0,4))
ax.set_xlim(min(x),max(x)), ax.set_xticks(np.arange(x[0],x[-1]+1,x[-1]/4))
ax.set_xlabel('x-distance',fontsize=15), ax.set_ylabel("altitude",fontsize=15)
ax.set_title("Airplane", fontsize=20)

# add text
bbox = dict(boxstyle='circle',fc=(0.8,0.8,0.8),ec='r',lw=5)
time_travel = ax.text(1400,0.65,'',fontsize=20,color='k',bbox=bbox)

bbox1 = dict(boxstyle='square',fc=(0.8,0.8,0.8),ec='r',lw=2)
dist_travel = ax.text(1000,0.5,'',fontsize=20,color='k',bbox=bbox1)

# ==================== Animation ======================================
animated_line, = ax.plot([],[],'r:o',linewidth=2)
plane_1, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing

# dotted points
dot = np.zeros(frames)
idx = 20
for i in range(0, frames):
    if i == idx:
        dot[i] = x[idx]
        idx+=20
    else:
        dot[i] = x[idx-20]


# static figure elements e.g houses -> skyscrapper
house_1 = ax.plot([100,100],[0,1],'k',linewidth=7)
house_2 = ax.plot([300,300],[0,1],'k',linewidth=7)
house_3 = ax.plot([700,700],[0,.7],'k',linewidth=15)
house_4 = ax.plot([900,900],[0,.9],'k',linewidth=10)
house_5 = ax.plot([1300,1300],[0,1],'k',linewidth=20)

# update the plot at each frame
def update_plot(frame):
    animated_line.set_data(dot[:frame], y[:frame])
    plane_1.set_data([x[frame]-50, x[frame]+50],[y[frame]])
    fwl.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]+0.4])
    fwr.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]-0.4])
    bwl.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]+0.18])
    bwr.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]-0.18])
    time_travel.set_text(f'{t[frame]:.1f} hrs')
    dist_travel.set_text(f'{int(x[frame])} km')

    return animated_line, fwl, fwr, bwl, bwr, plane_1

animation = FuncAnimation(fig, update_plot, frames=frames, interval=20, repeat=True)
plt.show()