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

# ====================== Airplane parameters ========================
# >>>>>> Airplane 1
a1 = 400
n1 = 2           # raise to power
x1 = a1*t**n1      # quadratic distance travel in kilometer
altitude1 = 2
y1 = np.ones(len(t))*altitude1    # altitude of the airplance

# >>>>> Airplane 2
a2 = 800
n2 = 1           # raise to power
x2 = a2*t**n2      # linear distance travel in kilometer
altitude2 = 1
y2 = np.ones(len(t))*altitude2    # altitude of the airplance

# >>>>> Airplane 3
a3 = 200
n3 = 3           # raise to power
x3 = a3*t**n3      # cubic distance travel in kilometer
altitude3 = 3
y3 = np.ones(len(t))*altitude3    # altitude of the airplance

# ======================== Figure and Axes ==========================
fig = plt.figure(figsize=(16,9), dpi = 120, facecolor=[0.8,0.8,0.8])
gs = GridSpec(2,2)

# >>>>>> Subplot 1
ax = fig.add_subplot(gs[0,:],facecolor=[0.9,0.9,0.9])
ax.set_ylim(0, max(y1)+2), ax.set_yticks(np.arange(0,4))
ax.set_xlim(min(x1),max(x1)/gain), ax.set_xticks(np.arange(x1[0],x1[-1]/gain+1,(x1[-1]/gain)/4))
ax.set_xlabel('x1-distance',fontsize=15), ax.set_ylabel("Altitude",fontsize=15)
ax.set_title("Airplane", fontsize=20)

# >>>>> Subplot 2
ax2 = fig.add_subplot(gs[1,0], facecolor=[0.9,0.9,0.9])
ax2.set_xlim(0,tf),ax2.set_ylim(min(x1),max(x1))
ax2.set_xlabel("Time (hrs)",fontsize=12), ax2.set_ylabel("Distance traveled (km)",fontsize=12)
ax2.set_xticks(np.arange(0,tf+dt,tf/4)),ax2.set_yticks(np.arange(min(x1),max(x1)+1,max(x1)/4))
ax2.set_title("Distance Vs Time", fontsize=15)

# >>>>>>> Subplot 3
ax3 = fig.add_subplot(gs[1,1], facecolor=[0.9, 0.9, 0.9])
ax3.set_xlim(0, max(t)), ax3.set_ylim(min(x1),max(x1))
ax3.set_ylabel("Speed (km/h)", fontsize=12), ax3.set_xlabel("Time (hrs)")
ax3.set_xticks(np.arange(t[0], max(t)+dt, max(t)/4)), ax3.set_yticks(np.arange(min(x1),max(x1)+1,max(x1)/4))
ax3.set_title("Speed Vs Time", fontsize=15)

# add text
speed_text = ax3.text(0.45, 1000, '', fontsize=12, color='k')


# =========================== Animation ===============================
# >>>>> Subplot 1
animated_line1, = ax.plot([],[],'r:o',linewidth=2)
plane_1, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl1, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr1, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl1, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr1, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing
vert_line1, = ax.plot([],[],'k:o',linewidth=1.5)

# >>> Airplane 2
animated_line2, = ax.plot([],[],'b:o',linewidth=2)
plane_2, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl2, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr2, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl2, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr2, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing
vert_line2, = ax.plot([],[],'k:o',linewidth=1.5)    

# >>> Airplane 3
animated_line3, = ax.plot([],[],'g:o',linewidth=2)
plane_3, = ax.plot([],[],'k',linewidth=10, solid_capstyle='butt')
fwl3, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front left wing
fwr3, = ax.plot([],[],'k',linewidth=5,solid_capstyle='butt')     # front right wing
bwl3, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back left wing
bwr3, = ax.plot([],[],'k',linewidth=4,solid_capstyle='butt')     # back right wing  
vert_line3, = ax.plot([],[],'k:o',linewidth=1.5)

# dotted points
dot1 = np.zeros(frames)
idx = int(20/gain)
for i in range(0, frames):
    if i == idx:
        dot1[i] = x1[idx]
        idx+=int(20/gain)
    else:
        dot1[i] = x1[idx-int(20/gain)]

dot2 = np.zeros(frames)
idx = int(20/gain)
for i in range(0, frames):
    if i == idx:
        dot2[i] = x2[idx]
        idx+=int(20/gain)
    else:
        dot2[i] = x2[idx-int(20/gain)]

dot3 = np.zeros(frames)
idx = int(20/gain)
for i in range(0, frames):
    if i == idx:
        dot3[i] = x3[idx]
        idx+=int(20/gain)
    else:
        dot3[i] = x3[idx-int(20/gain)]

# >>>>> Subplot 2
x_dist1, = ax2.plot([],[],'-r',linewidth=2,label=f"X1={a1}*t**{n1}")
# horizontal_line1, = ax2.plot([],[],'r:o',linewidth=1.5, label="distance")
# vertical_line1, = ax2.plot([],[],'g:o',linewidth=1.5, label="time")

# >>>> Airplane 2
x_dist2, = ax2.plot([],[],'-b',linewidth=2,label=f"X2={a2}*t**{n2}")
# horizontal_line2, = ax2.plot([],[],'r:o',linewidth=1.5, label="distance")
# vertical_line2, = ax2.plot([],[],'g:o',linewidth=1.5, label="time")   

# >>>> Airplane 3
x_dist3, = ax2.plot([],[],'-g',linewidth=2,label=f"X3={a3}*t**{n3}")
# horizontal_line3, = ax2.plot([],[],'r:o',linewidth=1.5, label="distance")
# vertical_line3, = ax2.plot([],[],'g:o',linewidth=1.5, label="time")   
ax2.legend(loc="upper left")

# >>>>> Subplot 3
speed, = ax3.plot([],[],'r',linewidth=2,label=r"$\frac{\Delta x1}{\Delta t}$"+f"= {n1*a1}t^{n1-1}")
# vert_ax3, = ax3.plot([],[],'k:o',linewidth=1.5, label="speed")

# >>>>> Speed of Airplane 2
speed2, = ax3.plot([],[],'b',linewidth=2,label=r"$\frac{\Delta x2}{\Delta t}$"+f"= {n2*a2}t^{n2-1}")
# vert_ax32, = ax3.plot([],[],'k:o',linewidth=1.5, label="speed")   

# >>>>> Speed of Airplane 3
speed3, = ax3.plot([],[],'g',linewidth=2,label=r"$\frac{\Delta x3}{\Delta t}$"+f"= {n3*a3}t^{n3-1}")
# vert_ax33, = ax3.plot([],[],'k:o',linewidth=1.5, label="speed")   

ax3.legend(loc="upper left")

# plot general function
plt.tight_layout()

# ========================= Slope of a function =============================
# Slope
slope = []
for i in range(0,frames):
    if i > 0:
        dydx = round((x1[i] - x1[i-1])/(t[i] - t[i-1]))
        slope.append(dydx)
    else:
        slope.append(0)

derivative1 = n1*a1*t**(n1-1) 
derivative2 = n2*a2*t**(n2-1)
derivative3 = n3*a3*t**(n3-1)

# ====================== Animation callback Function ============================
# update the plot at each frame
def update_plot(frame):
    # >>>> Subplot 1
    animated_line1.set_data(dot1[:frame], y1[:frame])
    plane_1.set_data([x1[frame]-50, x1[frame]+50],[y1[frame]])
    fwl1.set_data([x1[frame]+25,x1[frame]],[y1[frame], y1[frame]+0.4])
    fwr1.set_data([x1[frame]+25,x1[frame]],[y1[frame], y1[frame]-0.4])
    bwl1.set_data([x1[frame]-35,x1[frame]-50],[y1[frame], y1[frame]+0.18])
    bwr1.set_data([x1[frame]-35,x1[frame]-50],[y1[frame], y1[frame]-0.18])
    vert_line1.set_data([x1[frame]],[0,y1[frame]])

    animated_line2.set_data(dot2[:frame], y2[:frame])
    plane_2.set_data([x2[frame]-50, x2[frame]+50],[y2[frame]])
    fwl2.set_data([x2[frame]+25,x2[frame]],[y2[frame], y2[frame]+0.4]) 
    fwr2.set_data([x2[frame]+25,x2[frame]],[y2[frame], y2[frame]-0.4])
    bwl2.set_data([x2[frame]-35,x2[frame]-50],[y2[frame], y2[frame]+0.18])
    bwr2.set_data([x2[frame]-35,x2[frame]-50],[y2[frame], y2[frame]-0.18])
    vert_line2.set_data([x2[frame]],[0,y2[frame]])

    animated_line3.set_data(dot3[:frame], y3[:frame])
    plane_3.set_data([x3[frame]-50, x3[frame]+50],[y3[frame]])
    fwl3.set_data([x3[frame]+25,x3[frame]],[y3[frame], y3[frame]+0.4])
    fwr3.set_data([x3[frame]+25,x3[frame]],[y3[frame], y3[frame]-0.4])
    bwl3.set_data([x3[frame]-35,x3[frame]-50],[y3[frame], y3[frame]+0.18])
    bwr3.set_data([x3[frame]-35,x3[frame]-50],[y3[frame], y3[frame]-0.18])
    vert_line3.set_data([x3[frame]],[0,y3[frame]])

    # >>>>> Subplot 2
    x_dist1.set_data(t[:frame],x1[:frame])
    # horizontal_line1.set_data([t[0],t[frame]],[x1[frame]])
    # vertical_line1.set_data([t[frame]],[0,x1[frame]])

    x_dist2.set_data(t[:frame],x2[:frame])
    # horizontal_line2.set_data([t[0],t[frame]],[x2[frame]])
    # vertical_line2.set_data([t[frame]],[0,x2[frame]])   

    x_dist3.set_data(t[:frame],x3[:frame])
    # horizontal_line3.set_data([t[0],t[frame]],[x3[frame]])
    # vertical_line3.set_data([t[frame]],[0,x3[frame]])

    # >>>>>> Subplot 3
    # speed.set_data(t[:frame],slope[:frame])
    # vert_ax3.set_data([t[frame]],[0,slope[frame]])
    # speed_text.set_text(f'dy/dx = {int(slope[frame])} km/hr')

    speed.set_data(t[:frame],derivative1[:frame])
    # vert_ax3.set_data([t[frame]],[0,derivative1[frame]])
    # speed_text.set_text(f'Speed = {int(derivative1[frame])} km/hr')

    speed2.set_data(t[:frame],derivative2[:frame])
    # vert_ax32.set_data([t[frame]],[0,derivative2[frame]])
    # speed_text.set_text(f'Speed = {int(derivative2[frame])} km/hr')

    speed3.set_data(t[:frame],derivative3[:frame])
    # vert_ax33.set_data([t[frame]],[0,derivative3[frame]])
    # speed_text.set_text(f'Speed = {int(derivative3[frame])} km/hr')

    return animated_line1, fwl1, fwr1, bwl1, bwr1, vert_line1, plane_1, x_dist1, speed

# ====================== Display and Export Animation ==============================
animation = FuncAnimation(fig, update_plot, frames=frames, interval=20, repeat=True)
plt.show()