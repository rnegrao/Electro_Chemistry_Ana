import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import ScalarFormatter
from matplotlib.backends.backend_pdf import PdfPages
import itertools

#############################
#
#   QA Plots 
#
#############################

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

# create a document to save all the signals plot
outputfile = PdfPages("DATA_QA_GDC_all.pdf")###<-------------

# input file list
filelist1 = ["12112025/TEST_12112025_GDC9P9TON_T175C_3_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T200C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T225C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T250C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T275C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T300C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T325C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T350C_2_C01.txt"
            ]
filelist2 = ["12092025/TEST_12092025_GDC5P5TON_T175C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T200C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T225C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T250C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T275C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T300C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T325C_2_C01.txt",
             "12092025/TEST_12092025_GDC5P5TON_T350C_2_C01.txt"
            ]
filelist3 = ["12022025/TEST_12022025_GDC7TON_T175C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T200C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T225C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T250C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T275C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T300C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T325C_2_C01.txt",
             "12022025/TEST_12022025_GDC7TON_T350C_2_C01.txt",
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
filelist_all = ["12092025/TEST_12092025_GDC5P5TON_T175C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T200C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T225C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T250C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T275C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T300C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T325C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T350C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T175C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T200C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T225C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T250C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T275C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T300C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T325C_2_C01.txt",
            "12022025/TEST_12022025_GDC7TON_T350C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T175C_3_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T200C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T225C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T250C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T275C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T300C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T325C_2_C01.txt",
            "12112025/TEST_12112025_GDC9P9TON_T350C_2_C01.txt"
            ]
hex_colors_1 = ["#deebf7",
"#c6dbef",
"#9ecae1",
"#6baed6",
"#4292c6",
"#2171b5",
"#08519c",
"#08306b",
"#e5f5e0",
"#c7e9c0",
"#a1d99b",
"#74c476",
"#41ab5d",
"#238b45",
"#006d2c",
"#00441b",
"#fee5d9",
"#fcbba1",
"#fc9272",
"#fb6a4a",
"#ef3b2c",
"#cb181d",
"#a50f15",
"#67000d
    ]


 hex_colors_2 = [   "#67000D",
    "#A50F15",
    "#CB181D",
    "#EF3B2C",
    "#FB6A4A",
    "#FC9272",
    "#FCBBA1",
    "#FEE0D2",
    
    "#3D4989",
    "#30678D",
    "#25828D",
    "#1E9C88",
    "#35B778",
    "#6BCD58",
    "#B4DD2B",
    "#FDE724",
    
    "#08306B",
    "#08519C",
    "#2171B5",
    "#4292C6",
    "#6BAED6",
    "#9ECAE1",
    "#C6DBEF",
    "#DEEBF7"]

j=0
# Create the figure and axis
fig1, ax = plt.subplots(figsize=(8.5, 11))
for i in filelist_all:###<-------------
    data = np.loadtxt(i,skiprows=1)
    column1 = data[:,0]
    column2 = data[:,1]
    column3 = data[:,2]
    column4 = data[:,3]
    column5 = -1.0*data[:,4]
    
    # Create the Nyquist Impedance plot
    ax.loglog(column2,column3, label=i, marker='o',linestyle='None',color=hex_colors_1[j])
    #ax.plot(column2,column3, label=i, marker='o',linestyle='None',color=hex_colors_1[j])

    # Add labels and title
    plt.xlabel('Re[Z](Ohm)')
    plt.ylabel('-Im[Z](Ohm)')
    plt.title('Nyquist Impedance')
    plt.xlim(100,1200000)       # X-axis from  to 
    plt.ylim(10,1000000)  # Y-axis from  to 

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

    # Show the plot
    plt.tight_layout()
    
    j=j+1
    
outputfile.savefig()
plt.close()

# Create the figure and axis
fig2, ax = plt.subplots(figsize=(8.5, 11))
j=0
for i in filelist_all:###<-------------
    data1 = np.loadtxt(i,skiprows=1)
    column1 = data1[:,0]
    column2 = data1[:,1]
    column3 = data1[:,2]
    column4 = data1[:,3]
    column5 = -1.0*data1[:,4]
    
    # Create the Nyquist Impedance plot
    ax.semilogx(column1,column5, label=i, marker='o',linestyle='None',color=hex_colors_1[j])

    # Add labels and title
    plt.xlabel('Freq(Hz)')
    plt.ylabel('Phase(Z)/deg')
    plt.title('Bode Impedance')

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

    # Show the plot
    plt.tight_layout()
    
    j=j+1
    
outputfile.savefig()
plt.close()

# Close pdf file
outputfile.close()
print("Report created successfully!")
