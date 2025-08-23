import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation

# ======================== Parameters =============================
# simulation parameters
t0 = 0              # initial time in hours
tf = 2              # final time in hours
dt = 0.005          # time step
t = np.arange(t0, tf+dt, dt)
gain = 1            # change to make the plane move faster
frames = int(len(t)/gain)

# system parameter
x = 800*t*gain          # distance travel in kilometer
altitude = 2
y = np.ones(len(t))*altitude    # altitude of the airplance

# ======================== Figure and Axes ==========================
fig = plt.figure(figsize=(16,9), dpi = 120, facecolor=[0.8,0.8,0.8])
gs = GridSpec(2,2)

# >>>>>> Subplot 1
ax = fig.add_subplot(gs[0,:],facecolor=[0.9,0.9,0.9])
ax.set_ylim(0, max(y)+1), ax.set_yticks(np.arange(0,4))
ax.set_xlim(min(x),max(x)/gain), ax.set_xticks(np.arange(x[0],x[-1]/gain+1,(x[-1]/gain)/4))
ax.set_xlabel('x-distance',fontsize=15), ax.set_ylabel("Altitude",fontsize=15)
ax.set_title("Airplane", fontsize=20)

# add text
bbox = dict(boxstyle='circle',fc=(0.8,0.8,0.8),ec='r',lw=5)
time_travel = ax.text(1400,0.65,'',fontsize=20,color='k',bbox=bbox)

bbox1 = dict(boxstyle='square',fc=(0.8,0.8,0.8),ec='r',lw=2)
dist_travel = ax.text(1000,0.5,'',fontsize=20,color='k',bbox=bbox1)

# >>>>> Subplot 2
ax2 = fig.add_subplot(gs[1,0], facecolor=[0.9,0.9,0.9])
ax2.set_xlim(0,tf),ax2.set_ylim(min(x),max(x))
ax2.set_xlabel("Time (hrs)",fontsize=12), ax2.set_ylabel("Distance traveled (km)",fontsize=12)
ax2.set_xticks(np.arange(0,tf+dt,tf/4)),ax2.set_yticks(np.arange(min(x),max(x)+1,max(x)/4))
ax2.set_title("Distance Vs Time", fontsize=15)

# >>>>>>> Subplot 3
ax3 = fig.add_subplot(gs[1,1], facecolor=[0.9, 0.9, 0.9])
ax3.set_xlim(0, max(t)), ax3.set_ylim(min(x),max(x))
ax3.set_ylabel("Speed (km/h)", fontsize=12), ax3.set_xlabel("Time (hrs)")
ax3.set_xticks(np.arange(t[0], max(t)+dt, max(t)/4)), ax3.set_yticks(np.arange(min(x),max(x)+1,max(x)/4))
ax3.set_title("Speed Vs Time", fontsize=15)

# =========================== Animation ===============================
# >>>>> Subplot 1
animated_line, = ax.plot([],[],'r:o',linewidth=2)
plane_1, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing
vert_line, = ax.plot([],[],'k:o',linewidth=1.5)

# dotted points
dot = np.zeros(frames)
idx = int(20/gain)
for i in range(0, frames):
    if i == idx:
        dot[i] = x[idx]
        idx+=int(20/gain)
    else:
        dot[i] = x[idx-int(20/gain)]


# static figure elements e.g houses -> skyscrapper
house_1 = ax.plot([100,100],[0,1],'k',linewidth=7)
house_2 = ax.plot([300,300],[0,1],'k',linewidth=7)
house_3 = ax.plot([700,700],[0,.7],'k',linewidth=15)
house_4 = ax.plot([900,900],[0,.9],'k',linewidth=10)
house_5 = ax.plot([1300,1300],[0,1],'k',linewidth=20)

# >>>>> Subplot 2
x_dist, = ax2.plot([],[],'-b',linewidth=2,label="X=800*t")
horizontal_line, = ax2.plot([],[],'r:o',linewidth=1.5, label="distance")
vertical_line, = ax2.plot([],[],'g:o',linewidth=1.5, label="time")
ax2.legend(loc="upper left")

# >>>>> Subplot 3
speed, = ax3.plot([],[],'g',linewidth=2,label=r"$\frac{\Delta x}{\Delta t}$ = 800 km/h")
vert_ax3, = ax3.plot([],[],'k:o',linewidth=1.5, label="speed")
ax3.legend(loc="upper left")

# plot general function
plt.tight_layout()

# Slope
slope = []
for i in range(0,frames):
    if i > 0:
        dydx = round((x[i] - x[i-1])/(t[i] - t[i-1]))
        slope.append(dydx)
    else:
        slope.append(0)
    
# update the plot at each frame
def update_plot(frame):
    # >>>> Subplot 1
    animated_line.set_data(dot[:frame], y[:frame])
    plane_1.set_data([x[frame]-50, x[frame]+50],[y[frame]])
    fwl.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]+0.4])
    fwr.set_data([x[frame]+25,x[frame]],[y[frame], y[frame]-0.4])
    bwl.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]+0.18])
    bwr.set_data([x[frame]-35,x[frame]-50],[y[frame], y[frame]-0.18])
    time_travel.set_text(f'{t[frame]*gain:.1f} hrs')
    dist_travel.set_text(f'{int(x[frame])} km')
    vert_line.set_data([x[frame]],[0,y[frame]])

    # >>>>> Subplot 2
    x_dist.set_data(t[:frame],x[:frame])
    horizontal_line.set_data([t[0],t[frame]],[x[frame]])
    vertical_line.set_data([t[frame]],[0,x[frame]])

    # >>>>>> Subplot 3
    speed.set_data(t[:frame],slope[frame])
    vert_ax3.set_data([t[frame]],[0,slope[frame]])

    return animated_line, fwl, fwr, bwl, bwr, vert_line, plane_1, x_dist, speed

# ====================== Display and Export Animation ==============================
animation = FuncAnimation(fig, update_plot, frames=frames, interval=20, repeat=True)
plt.show()