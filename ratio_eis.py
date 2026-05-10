# ratio_eis.py
# Plot ration of the user provided data.
# Requirements: numpy, matplotlib, lmfit
# Install: pip install numpy matplotlib lmfit

import math
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Parameters, minimize, report_fit
from matplotlib.ticker import ScalarFormatter

# ----------  ----------

hex_colors = [
            "#67000D",
            "#A50F15",
            "#CB181D",
            "#EF3B2C",
            "#FB6A4A",
            "#FC9272",
            "#FCBBA1",
            "#FEE0D2"
            ]

####################################
# Parse DATA
####################################
data = np.loadtxt("DATA/CERAMIC_PROBE_TEST/TEST_CERAMIC_PROBE_AND_AUTOLAB_DUMMYCELLb_2_C01.txt",skiprows=1)
f = data[:,0]
Re = data[:,1]
Im = data[:,2]
Z = data[:,3]

data1 = np.loadtxt("DATA/CERAMIC_PROBE_TEST/TEST_AUTOLAB_DUMMYCELLb__C01.txt",skiprows=1)
f1 = data[:,0]
Re1 = data[:,1]
Im1 = data[:,2]
Z1 = data[:,3]

####################################
# PLOT NYQUIST
####################################

fig, ax = plt.subplots(figsize=(12, 8))
plt.plot(Re, Im, 'o', label='EIS Measurements - Ceramic Probe into CE path', markersize=6,color=hex_colors[1])
plt.plot(Re1, Im1, 'D', label='EIS Measurements - Dummy cell only',  markersize=4,color=hex_colors[5])
plt.xlabel('Re(Z) / Ohm')
plt.ylabel('Im(Z) / Ohm')
plt.title('')

# Set font to sans-serif for a scientific look
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'mathtext.fontset': 'cm',
})

# Scientific notation on both axes
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

# Add grid, minor ticks, and legend
ax.grid(True, which='major', linestyle='-', alpha=0.3)
ax.minorticks_on()
ax.grid(True, which='minor', linestyle=':', alpha=0.2)
ax.legend(loc='upper left',frameon=False)
        
plt.legend()
plt.savefig('ceramict_test_plot.png', dpi=300)
plt.show()

####################################
# PLOT ratio
####################################

fig1, ax1 = plt.subplots(figsize=(12, 5))
plt.plot(5*f, Z/Z1, 'o', label='Ratio between impedance measurements Z$_{Probe}$/Z$_{No Probe}$', markersize=6,color=hex_colors[1])
#plt.plot(Re1, Im1, 'D', label='EIS Measurements',  markersize=4,color=hex_colors[5])
plt.xlabel('Freq / Hz')
plt.ylabel('Z$_{Probe}$/Z$_{No Probe}$ ')
plt.title('')

# Set font to sans-serif for a scientific look
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
    'mathtext.fontset': 'cm',
})

# Scientific notation on both axes
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
ax1.xaxis.set_major_formatter(formatter)
ax1.yaxis.set_major_formatter(formatter)

# Add grid, minor ticks, and legend
ax1.grid(True, which='major', linestyle='-', alpha=0.3)
ax1.minorticks_on()
ax1.grid(True, which='minor', linestyle=':', alpha=0.2)
ax1.legend(loc='upper left',frameon=False)
        
plt.legend()
plt.savefig('ceramict_test_ratio_plot.png', dpi=300)
plt.show()
