import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation

# set the duration for the animation
t0 = 0          # in hours (hrs)
tf = 2          # in hours (hrs)
dt = 0.005      # in hours (hrs)
t = np.arange(t0,tf+dt,dt)

# create x array
x = 100 * t     # in km

# create y array
altitude = 2
y = np.ones(len(t)) * 2     # in km


# ==================== Animation ========================= #
frame_amount = len(t)

def update_plot(num):
    plane_trajectory.set_data(x[0:num], y[0:num])
    return plane_trajectory,

fig = plt.figure(figsize=(16,9), dpi=120, facecolor=[0.8, 0.8, 0.8])
gs = gridspec.GridSpec(2,2)

# subplot
ax0 = fig.add_subplot(gs[0,:], facecolor=[0.9, 0.9, 0.9])
plane_trajectory, = ax0.plot([],[],'g',linewidth=2)
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)

plane_animate = animation.FuncAnimation(fig,update_plot,frames=frame_amount, 
                                        interval=20, repeat=True)
plt.show()
