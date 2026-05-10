# Arrhenius_conductivity.py
# Plot user-provided Arrhenius plot
# Requirements: numpy, matplotlib, lmfit
# Install: pip install numpy matplotlib lmfit

import math
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Parameters, minimize, report_fit
from matplotlib.ticker import ScalarFormatter

# ----------  ----------
# file list
file_list_gdc = [
            "DATA/CONDUCTIVITY/GDC_6P5TON_CONDUCTIVITY_VS_1OVERT.txt",
            "DATA/CONDUCTIVITY/GDC_REF1_CONDUCTIVITY_VS_1OVERT.txt",
            "DATA/CONDUCTIVITY/GDC_REF2_CONDUCTIVITY_VS_1OVERT.txt"
            ]
legend_string_gdc = [
            "CNPEM measurements (GDC)",
            "Reference https://doi.org/10.1007/s42452-020-03280-2",
            "Reference https://doi.org/10.1039/D4MA00690A"
            ]

file_list_lsgm = [
            "DATA/CONDUCTIVITY/LSGM_CONDUCTIVITY_VS_1OVERT.txt",
            "DATA/CONDUCTIVITY/LSGM_REF1_CONDUCTIVITY_VS_1OVERT.txt",
            "DATA/CONDUCTIVITY/LSGM_REF2_CONDUCTIVITY_VS_1OVERT.txt"
            ]
legend_string_lsgm = [
            "CNPEM measurements (LSGM)",
            "https://doi.org/10.3390/membranes13050502",
            "https://doi.org/10.1039/D4MA00690A"
            ]

hex_colors = ["#202020",
              "#67000D",
            "#286484",
            

            "#286484",
            "#08519C",
            "#2F7CAA",

            "#67000D",
            "#A50F15",
            "#CB181D",
            "#EF3B2C",
            "#FB6A4A",
            "#FC9272",
            "#FCBBA1",
            "#FEE0D2"
            ]
maker_style = [
            'o',
            's',
            'D',
            'P',
            'X',
            'p',
            '^'
            ]

j=0
fig, ax = plt.subplots(figsize=(8, 8))

for i in file_list_gdc:
    ####################################
    # Parse DATA
    ####################################
    data = np.loadtxt(i,skiprows=2)
    sigma = data[:,1]
    InvT = data[:,2]

    ####################################
    # PLOT 
    ####################################
    #plt.plot(sigma, InvT, 'o', label=legend_string_gdc[j], markersize=4,color=hex_colors[j])
    plt.semilogy(sigma, InvT, 'o', marker=maker_style[j], label=legend_string_gdc[j], markersize=4,color=hex_colors[j])
    plt.xlabel('1000/T (1/K)')
    plt.ylabel(' Conductivity (S/cm)')
    plt.title('')
    j=j+1

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
    #ax.xaxis.set_major_formatter(formatter)
    #ax.yaxis.set_major_formatter(formatter)

    # Add grid, minor ticks, and legend
    ax.grid(True, which='major', linestyle='-', alpha=0.3)
    ax.minorticks_on()
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    ax.legend(loc='upper left',frameon=False)
            
    plt.legend()
    #plt.savefig(figfile, dpi=300)

plt.show()
#print("Saved figure:", figfile)

