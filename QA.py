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

filelist_all = [
            "01072026/TEST_01072026_GDC4P5TON_T175C_3_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T200C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T225C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T250C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T275C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T300C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T325C_2_C01.txt",
            "01072026/TEST_01072026_GDC4P5TON_T350C_2_C01.txt",
                
            "12092025/TEST_12092025_GDC5P5TON_T175C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T200C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T225C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T250C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T275C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T300C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T325C_2_C01.txt",
            "12092025/TEST_12092025_GDC5P5TON_T350C_2_C01.txt",

            "01092026/TEST_01092026_GDC6P5TON_T175C_3_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T200C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T225C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T250C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T275C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T300C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T325C_2_C01.txt",
            "01092026/TEST_01092026_GDC6P5TON_T350C_2_C01.txt",
                
            "01192026/TEST_01192026_GDC7P2TON_T178C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T203C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T228P5C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T254C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T279C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T305C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T330C_2_C01.txt",
            "01192026/TEST_01192026_GDC7P2TON_T355P5C_2_C01.txt",

            "01132026/TEST_01132026_GDC8P1TON_T175C_3_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T200C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T225C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T250C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T275C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T300C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T325C_2_C01.txt",
            "01132026/TEST_01132026_GDC8P1TON_T350C_2_C01.txt",
            
            "01152026/TEST_01152026_GDC9TON_T176C_3_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T201C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T226C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T251C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T277C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T303C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T328C_2_C01.txt",
            "01152026/TEST_01152026_GDC9TON_T353C_2_C01.txt"

            ]

hex_colors_1 = [
                
            "#08306b",
            "#08519c",
            "#2171b5",
            "#4292c6",
            "#6baed6",
            "#9ecae1",
            "#c6dbef",
            "#deebf7",
                            
            "#00441B",
            "#006D2C",
            "#238B45",
            "#41AE76",
            "#66C2A4",
            "#99D8C9",
            "#CCECE6",
            "#E5F5F9",
                            
            "#67000d",
            "#a50f15",
            "#cb181d",
            "#ef3b2c",
            "#fb6a4a",
            "#fc9272",
            "#fcbba1",                
            "#fee5d9",

            "#242424",
            "#404040",
            "#545454",
            "#515151",
            "#8D8D8D",
            "#AFAFAF",
            "#C0C0C0",
            "#D2D2D2",

            "#7F2704",
            "#A63603",
            "#D94801",
            "#F16913",
            "#FD8D3C",
            "#FDAE6B",
            "#FDD0A2",
            "#FEE6CE",
                            
            "#4D3B00",
            "#7A5C00",
            "#B38A00",
            "#E6B800",
            "#FFD24D",
            "#FFE680",
            "#FFF0B3",
            "#FFF7D6"
            ]

j=0
# Create the figure and axis
fig1, ax = plt.subplots(figsize=(25.5, 33))
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
fig2, ax = plt.subplots(figsize=(25.5, 33))
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

# Create the figure and axis

hex_colors_2 = ["#CB181D",
                "#CB181D",
                "#CB181D",
                "#CB181D",
                "#CB181D",
                "#CB181D",
                "#CB181D",
                "#CB181D",
                
               
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                "#EF3B2C",
                
                "#08519C",
                "#08519C",
                "#08519C",
                "#08519C",
                "#08519C",
                "#08519C",
                "#08519C",
                "#08519C",
                
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                "#2F7CAA",
                
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",

    ]

fig3, ax = plt.subplots(figsize=(25.5, 33))
j=0
for i in filelist_all:###<-------------
    data2 = np.loadtxt(i,skiprows=1)
    column1 = data2[:,0]
    column2 = data2[:,1]
    column3 = data2[:,2]
    column4 = data2[:,3]
    column5 = -1.0*data2[:,4]
    
    # Create the Nyquist Impedance plot
    #ax.loglog(column2,column3, label=i, marker='o',linestyle='None',color=hex_colors_1[j])
    ax.plot(column2,column3, label=i, marker='o',linestyle='None',color=hex_colors_2[j])

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

plt.show()

# Close pdf file
outputfile.close()
print("Report created successfully!")
