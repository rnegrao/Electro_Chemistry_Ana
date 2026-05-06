# fit_eis.py
# Plot user-provided Nyquist data (Re, Im) to 2x (R || CPE) in series.
# Requirements: numpy, matplotlib, lmfit
# Install: pip install numpy matplotlib lmfit

import math
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Parameters, minimize, report_fit
from matplotlib.ticker import ScalarFormatter

####################################
# Model definitions
####################################
def Z_CPE(Q, n, w):
    return 1.0/(Q*(1j*w)**n)

def Z_R_par_CPE(R, Q, n, w):
    Zcpe = Z_CPE(Q, n, w)
    return 1.0 / (1.0/R + 1.0/Zcpe)

def Wd(Rd, td, w):
    return Rd*np.tanh(np.sqrt(td*(1j*w))) / np.sqrt(td*(1j*w))

def model_complex(params, w):
    R0 = params['R0'].value
    R1 = params['R1'].value; Q1 = params['Q1'].value; n1 = params['n1'].value
    R2 = params['R2'].value; Q2 = params['Q2'].value; n2 = params['n2'].value
    Rd = params['Rd'].value; td = params['td'].value; 
    return (R0 +
            Z_R_par_CPE(R1, Q1, n1, w) +
            Z_R_par_CPE(R2, Q2, n2, w) +
            Wd(Rd, td, w))

# residual for fitting
def residual(params, w, data_complex):
    Zm = model_complex(params, w)
    res = np.concatenate([(Zm.real - data_complex.real), (Zm.imag - data_complex.imag)])
    return res

# ---------- your freq/Hz Re(Z)/Ohm -Im(Z)/Ohm |Z|/Ohm Phase(Z)/deg data ----------
# file list
file_list = [
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T175C_3_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T200C_2_C01.txt",
            #"DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T225C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T250C_2_C01.txt",
            #"DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T275C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T300C_2_C01.txt",
            #"DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T325C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T350C_2_C01.txt",
                
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T175C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T200C_2_C01.txt",
            #"DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T225C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T250C_2_C01.txt",
            #"DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T275C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T300C_2_C01.txt",
            #"DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T325C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T350C_2_C01.txt",

            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T175C_3_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T200C_2_C01.txt",
            #"DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T225C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T250C_2_C01.txt",
            #"DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T275C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T300C_2_C01.txt",
            #"DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T325C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T350C_2_C01.txt",
                
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T175C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T200C_2_C01.txt",
            #"DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T225C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T250C_2_C01.txt",
            #"DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T275C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T300C_2_C01.txt",
            #"DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T325C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T350C_2_C01.txt",

            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T175C_3_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T200C_2_C01.txt",
            #"DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T225C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T250C_2_C01.txt",
            #"DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T275C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T300C_2_C01.txt",
            #"DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T325C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T350C_2_C01.txt",
            
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T175C_3_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T200C_2_C01.txt",
            #"DATA/GDC9TON/TEST_01152026_GDC9TON_T225C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T250C_2_C01.txt",
            #"DATA/GDC9TON/TEST_01152026_GDC9TON_T275C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T300C_2_C01.txt",
            #"DATA/GDC9TON/TEST_01152026_GDC9TON_T325C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T350C_2_C01.txt",

            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T175C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T200C_2_C01.txt",
            #"DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T225C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T250C_2_C01.txt",
            #"DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T275C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T300C_2_C01.txt",
            #"DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T325C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T350C_2_C01.txt"
            ]

legend_string = [
            "GDC 4.5TON T=175C",
            "GDC 4.5TON T=200C",
            #"GDC 4.5TON T=225C",
            "GDC 4.5TON T=250C",
            #"GDC 4.5TON T=275C",
            "GDC 4.5TON T=300C",
            #"GDC 4.5TON T=325C",
            "GDC 4.5TON T=350C",
                
            "GDC 5.5TON T=175C",
            "GDC 5.5TON T=200C",
            #"GDC 5.5TON T=225C",
            "GDC 5.5TON T=250C",
            #"GDC 5.5TON T=275C",
            "GDC 5.5TON T=300C",
            #"GDC 5.5TON T=325C",
            "GDC 5.5TON T=350C",

            "GDC 6.5TON T=175C",
            "GDC 6.5TON T=200C",
            #"GDC 6.5TON T=225C",
            "GDC 6.5TON T=250C",
            #"GDC 6.5TON T=275C",
            "GDC 6.5TON T=300C",
            #"GDC 6.5TON T=325C",
            "GDC 6.5TON T=350C",
                
            "GDC 7.2TON T=175C",
            "GDC 7.2TON T=200C",
            #"GDC 7.2TON T=225C",
            "GDC 7.2TON T=250C",
            #"GDC 7.2TON T=275C",
            "GDC 7.2TON T=300C",
            #"GDC 7.2TON T=325C",
            "GDC 7.2TON T=350C",

            "GDC 8.1TON T=175C",
            "GDC 8.1TON T=200C",
            #"GDC 8.1TON T=225C",
            "GDC 8.1TON T=250C",
            #"GDC 8.1TON T=275C",
            "GDC 8.1TON T=300C",
            #"GDC 8.1TON T=325C",
            "GDC 8.1TON T=350C",

            "GDC 9.0TON T=175C",
            "GDC 9.0TON T=200C",
            #"GDC 9.0TON T=225C",
            "GDC 9.0TON T=250C",
            #"GDC 9.0TON T=275C",
            "GDC 9.0TON T=300C",
            #"GDC 9.0TON T=325C",
            "GDC 9.0TON T=350C",

            "GDC 9.9TON T=175C",
            "GDC 9.9TON T=200C",
            #"GDC 9.9TON T=225C",
            "GDC 9.9TON T=250C",
            #"GDC 9.9TON T=275C",
            "GDC 9.9TON T=300C",
            #"GDC 9.9TON T=325C",
            "GDC 9.9TON T=350C"
            ]

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


input_parameters=[
            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000],

            [10,297000,1.5100e-10,0.85,36629,14.96E-9,1.1,35429400,91796],
            [10,84558,0.235e-9,0.85,8000,90e-09,1.0,45000000,50000],
            [10,10005,0.35e-9,0.85,500,150e-09,0.95,40000000,75000],
            [0,1750,0.35e-9,0.99,100.0,1e-12,1.0,4000000,55000],
            [0,510,1.0e-11,0.99,0.1,1e-12,1.0,4000000,55000]
            ]

j=0

for i in file_list:
        ####################################
        # Parse DATA
        ####################################
        data = np.loadtxt(i,skiprows=1)
        Re = data[10:100,1]
        Im = data[10:100,2]

        Z_data = Re + 1j*Im  # NOTE: if Im in your file is -Im, modify accordingly

        N = len(Z_data)
        print("Points loaded:", N)
        
        ####################################
        # FREQUENCY ASSUMPTION
        ####################################
        # If you have the real frequencies, replace this vector with them (one value per point).
        f_max = 3e6
        f_min = .5e0
        freqs = np.logspace(np.log10(f_max), np.log10(f_min), N)
        omega = 2*np.pi*freqs

        ####################################
        # Initial parameters & bounds
        ####################################
        n=1.
        R0=input_parameters[j][0]
        R1=input_parameters[j][1]
        Q1=input_parameters[j][2]
        n1=input_parameters[j][3]
        R2=input_parameters[j][4]
        Q2=input_parameters[j][5]
        n2=input_parameters[j][6]
        Rd=input_parameters[j][7]
        td=input_parameters[j][8]

        params = Parameters()

        #resistance
        params.add('R0', value=R0, vary=False)
        #first circle
        params.add('R1', value=R1, min=R1-n*R1, max=R1+n*R1, vary=False)
        params.add('Q1', value=Q1, min=Q1-n*Q1, max=Q1+n*Q1, vary=False)
        params.add('n1', value=n1, min=n1-n*n1, max=n1+n*n1, vary=False)
        #second circle
        params.add('R2', value=R2, min=R2-n*R2, max=R2+n*R2, vary=True)
        params.add('Q2', value=Q2, min=Q2-n*Q2, max=Q2+n*Q2, vary=True)
        params.add('n2', value=n2, min=n2-n*n2, max=n2+n*n2, vary=True)
        #diffusion
        params.add('Rd', value=Rd, min=Rd-n*Rd, max=Rd+n*Rd, vary=False)
        params.add('td', value=td, min=td-n*td, max=td+n*td, vary=False)

        # Run minimization
        result = minimize(residual, params, args=(omega, Z_data), method='leastsq', max_nfev=20000)

        # Report
        print("\nFit report:")
        report_fit(result.params)

        # Extract fit model
        Z_fit = model_complex(result.params, omega)

        ####################################
        # PLOT NYQUIST
        ####################################
        
        figfile = i+'.png'
        fig, ax = plt.subplots(figsize=(8, 8))
        plt.plot(Re, Im, 'o', label='EIS Measurements '+i, markersize=4,color=hex_colors[1])
        j=j+1
        plt.plot(Z_fit.real, -Z_fit.imag, '--', label='Equivalent Circuit Model', linewidth=1)
        plt.xlabel('Re(Z) / Ohm')
        plt.ylabel('Im(Z) / Ohm')
        plt.title('Nyquist plot (data vs fit)')
    
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
        #plt.savefig(figfile, dpi=300)
        plt.show()
        print("Saved figure:", figfile)

        # In case you have pellet thickness (L) and electrode area (A), compute conductivity:
        # sigma = L / (R_bulk * A)
