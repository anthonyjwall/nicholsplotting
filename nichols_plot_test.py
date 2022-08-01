from scipy import signal
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm
import control


## Setting some common constants

pi = math.pi

# Setting s as the laplace variable
s = control.tf('s')

# setting j as the square root of -1
j = complex(0,1)

# Creating the magnitude and phase sweep
mag_sweep = np.logspace(np.log10(0.001), np.log10(1000), num=500, base=10)
phase_sweep = np.linspace(-360, 0, 500)

# Creating a frequency sweep for the system
f_sweep = np.logspace(np.log10(0.001), np.log10(100), num=500, base=10 )
f_sweep = np.concatenate((-f_sweep, f_sweep))
w_sweep = 2*pi*f_sweep

# Creating a system to plot on the Nichols plot
#TF_sys_LG = 1 / (1-s)
#TF_sys_LG = 1 / ( (1+s) * (1+s) )
TF_sys_LG = 60 * ((s/2)+1) / ( ((s/10) - 1) * ((10*s) + 1) * ((s/100) + 1) * ((s/1000) + 1) * ((s/10000) + 1) )

plt.figure(1)
control.bode(TF_sys_LG, omega=w_sweep, dB=True)

# Creating a meshgrid of the magnitude and phase
mag_sweep, phase_sweep = np.meshgrid(mag_sweep, phase_sweep)

# Creating a variable containing all values of (open) loopgain
G = mag_sweep * np.exp(j*phase_sweep*pi/180)

# Creating the Closed-loop transfer function resulting from the LG
H = G / (1+G)
H_mag_dB = control.mag2db(np.abs(H))


# Plotting the 3D Nichols Surface
plt.figure(2)
ax = plt.axes(projection='3d')
ax.plot_surface(control.mag2db(mag_sweep), phase_sweep, H_mag_dB, cmap=cm.viridis, alpha=0.75, zorder=1)



# Calculating the magnitude and phase of the system LG
sys_LG_mag, sys_LG_phase, tmp = control.bode(TF_sys_LG, omega=w_sweep, plot=False)
sys_LG_mag = control.mag2db(sys_LG_mag)
sys_LG_phase = sys_LG_phase * (180/pi)

#TF_sys_CL = TF_sys_LG/(1+TF_sys_LG)
TF_sys_CL = control.feedback(TF_sys_LG, 1)

sys_CL_mag, sys_CL_phase, tmp = control.bode(TF_sys_CL, omega=w_sweep, plot=False)
sys_CL_mag = control.mag2db(sys_CL_mag)
sys_CL_phase = sys_CL_phase * (180/pi)

# Adding the system to the Nichols plot
ax.plot(sys_LG_mag, sys_LG_phase, sys_CL_mag, zorder=10)



# Plotting a first order system
#tf_1ord = 1 / (1+s)

#mag,phase,w = control.bode(tf_1ord, Hz=True, dB=True, Plot=False)

# plt.figure()
# plt.plot(w, control.mag2db(mag))
# plt.xscale('log')
# plt.yscale('linear')
# plt.grid()


# plt.figure()
# plt.plot(w, (180/math.pi)*phase)
# plt.xscale('log')
# plt.yscale('linear')
# plt.grid()

plt.show()

print("pause")