import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import ScalarFormatter
from matplotlib.backends.backend_pdf import PdfPages
import itertools

filelist_all = [
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T175C_3_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T200C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T225C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T250C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T275C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T300C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T325C_2_C01.txt",
            "DATA/GDC4P5TON/TEST_01072026_GDC4P5TON_T350C_2_C01.txt",
                
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T175C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T200C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T225C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T250C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T275C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T300C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T325C_2_C01.txt",
            "DATA/GDC5P5TON/TEST_12092025_GDC5P5TON_T350C_2_C01.txt",

            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T175C_3_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T200C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T225C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T250C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T275C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T300C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T325C_2_C01.txt",
            "DATA/GDC6P5TON/TEST_01092026_GDC6P5TON_T350C_2_C01.txt",
                
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T175C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T200C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T225C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T250C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T275C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T300C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T325C_2_C01.txt",
            "DATA/GDC7P2TON/TEST_01192026_GDC7P2TON_T350C_2_C01.txt",

            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T175C_3_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T200C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T225C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T250C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T275C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T300C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T325C_2_C01.txt",
            "DATA/GDC8P1TON/TEST_01132026_GDC8P1TON_T350C_2_C01.txt",
            
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T175C_3_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T200C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T225C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T250C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T275C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T300C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T325C_2_C01.txt",
            "DATA/GDC9TON/TEST_01152026_GDC9TON_T350C_2_C01.txt",

            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T175C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T200C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T225C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T250C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T275C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T300C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T325C_2_C01.txt",
            "DATA/GDC9P9TON/TEST_01222026_GDC9P9TON_T350C_2_C01.txt"
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

            "#50187E",
            "#5C1F93",
            "#6928A8",
            "#783BBE",
            "#8A56D2",
            "#9F75E3",
            "#B899F0",
            "#D0C1FA",

            "#73003F",
            "#88004D",
            "#9D005B",
            "#B20069",
            "#C71A7A",
            "#DB3C8F",
            "#EC6FA7",
            "#F39BC0",
                        
            "#006634",
            "#007D3E",
            "#1E944F",
            "#3CAB65",
            "#5EC07C",
            "#82D59A",
            "#A7E6B8",
            "#C7F1D2",

            "#645000",
            "#7A6200",
            "#917500",
            "#A88900",
            "#C09D00",
            "#D8B200",
            "#EFC84D",
            "#FFE08A",
            
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
            "#D2D2D2"               
            ]

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
                
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                "#67000D",
                
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",
                "#A50F15",

                "#404040",
                "#404040",
                "#404040",
                "#404040",
                "#404040",
                "#404040",
                "#404040",
                "#404040"
                ]

hex_colors_3 = ["#CB181D",
                "#EF3B2C",
                
                "#08519C",
                "#2F7CAA",
      
                "#67000D",
                "#A50F15",

                "#404040"
                ]

hex_colors_4 = [
        "#565656",
        "#6B6B6B",
        "#808080",
        "#969696",
        "#ACACAC",
        "#C2C2C2",
        "#D8D8D8"
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
    
def QA_plot():
    #############################
    #   QA Plots 
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

    #########################################
    # Create QA figure and generate 
    # Nyquist plot
    #########################################
    fig1, ax = plt.subplots(figsize=(25.5, 33))
    j=0
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

    #########################################
    # Create QA figure and generate 
    # Bode plot
    #########################################
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
    #########################################
    # Close pdf file
    #########################################
    outputfile.close()
    print("Report created successfully!")

def nyquist_plot_all():
    #########################################
    # Create figure and generate 
    #########################################

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

def nyquist_plot_by_temperature():
    #########################################
    # Nyquist Plot of all data by temperature
    #########################################
    legend_string = [
                "GDC 4.5TON T=175C",
                "GDC 4.5TON T=200C",
                "GDC 4.5TON T=225C",
                "GDC 4.5TON T=250C",
                "GDC 4.5TON T=275C",
                "GDC 4.5TON T=300C",
                "GDC 4.5TON T=325C",
                "GDC 4.5TON T=350C",
                    
                "GDC 5.5TON T=175C",
                "GDC 5.5TON T=200C",
                "GDC 5.5TON T=225C",
                "GDC 5.5TON T=250C",
                "GDC 5.5TON T=275C",
                "GDC 5.5TON T=300C",
                "GDC 5.5TON T=325C",
                "GDC 5.5TON T=350C",

                "GDC 6.5TON T=175C",
                "GDC 6.5TON T=200C",
                "GDC 6.5TON T=225C",
                "GDC 6.5TON T=250C",
                "GDC 6.5TON T=275C",
                "GDC 6.5TON T=300C",
                "GDC 6.5TON T=325C",
                "GDC 6.5TON T=350C",
                    
                "GDC 7.2TON T=175C",
                "GDC 7.2TON T=200C",
                "GDC 7.2TON T=225C",
                "GDC 7.2TON T=250C",
                "GDC 7.2TON T=275C",
                "GDC 7.2TON T=300C",
                "GDC 7.2TON T=325C",
                "GDC 7.2TON T=350C",

                "GDC 8.1TON T=175C",
                "GDC 8.1TON T=200C",
                "GDC 8.1TON T=225C",
                "GDC 8.1TON T=250C",
                "GDC 8.1TON T=275C",
                "GDC 8.1TON T=300C",
                "GDC 8.1TON T=325C",
                "GDC 8.1TON T=350C",
                
                "GDC 9.0TON T=175C",
                "GDC 9.0TON T=200C",
                "GDC 9.0TON T=225C",
                "GDC 9.0TON T=250C",
                "GDC 9.0TON T=275C",
                "GDC 9.0TON T=300C",
                "GDC 9.0TON T=325C",
                "GDC 9.0TON T=350C",

                "GDC 9.9TON T=175C",
                "GDC 9.9TON T=200C",
                "GDC 9.9TON T=225C",
                "GDC 9.9TON T=250C",
                "GDC 9.9TON T=275C",
                "GDC 9.9TON T=300C",
                "GDC 9.9TON T=325C",
                "GDC 9.9TON T=350C"
                ]
    legend_string = [
                "GDC 63.7 MPa T=175C",
                "GDC 63.7 MPa T=200C",
                "GDC 63.7 MPa T=225C",
                "GDC 63.7 MPa T=250C",
                "GDC 63.7 MPa T=275C",
                "GDC 63.7 MPa T=300C",
                "GDC 63.7 MPa T=325C",
                "GDC 63.7 MPa T=350C",
                    
                "GDC 77.8 MPa T=175C",
                "GDC 77.8 MPa T=200C",
                "GDC 77.8 MPa T=225C",
                "GDC 77.8 MPa T=250C",
                "GDC 77.8 MPa T=275C",
                "GDC 77.8 MPa T=300C",
                "GDC 77.8 MPa T=325C",
                "GDC 77.8 MPa T=350C",

                "GDC 91.9 MPa T=175C",
                "GDC 91.9 MPa T=200C",
                "GDC 91.9 MPa T=225C",
                "GDC 91.9 MPa T=250C",
                "GDC 91.9 MPa T=275C",
                "GDC 91.9 MPa T=300C",
                "GDC 91.9 MPa T=325C",
                "GDC 91.9 MPa T=350C",
                    
                "GDC 101.8 MPa T=175C",
                "GDC 101.8 MPa T=200C",
                "GDC 101.8 MPa T=225C",
                "GDC 101.8 MPa T=250C",
                "GDC 101.8 MPa T=275C",
                "GDC 101.8 MPa T=300C",
                "GDC 101.8 MPa T=325C",
                "GDC 101.8 MPa T=350C",

                "GDC 114.6 MPa T=175C",
                "GDC 114.6 MPa T=200C",
                "GDC 114.6 MPa T=225C",
                "GDC 114.6 MPa T=250C",
                "GDC 114.6 MPa T=275C",
                "GDC 114.6 MPa T=300C",
                "GDC 114.6 MPa T=325C",
                "GDC 114.6 MPa T=350C",
                
                "GDC 127.3 MPa T=175C",
                "GDC 127.3 MPa T=200C",
                "GDC 127.3 MPa T=225C",
                "GDC 127.3 MPa T=250C",
                "GDC 127.3 MPa T=275C",
                "GDC 127.3 MPa T=300C",
                "GDC 127.3 MPa T=325C",
                "GDC 127.3 MPa T=350C",

                "GDC 140.0 MPa T=175C",
                "GDC 140.0 MPa T=200C",
                "GDC 140.0 MPa T=225C",
                "GDC 140.0 MPa T=250C",
                "GDC 140.0 MPa T=275C",
                "GDC 140.0 MPa T=300C",
                "GDC 140.0 MPa T=325C",
                "GDC 140.0 MPa T=350C"
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
    
    for i in range(0,8): # TEMPERATURE LOOP
        fig4, ax = plt.subplots(figsize=(8, 8))
        for j in range(0,7,3): #SAMPLE LOOP
            
            data3 = np.loadtxt(filelist_all[j*8+i],skiprows=13)
            print(filelist_all[j*8+i])
            column1 = data3[:,0]
            column2 = data3[:,1]
            column3 = data3[:,2]
            column4 = data3[:,3]
            column5 = -1.0*data3[:,4]
            
            # Create the Nyquist Impedance plot
            #ax.loglog(column2,column3, label=i, marker='o',linestyle='None',color=hex_colors_1[j])
            ax.plot(column2,column3, label=legend_string[j*8+i], marker=maker_style[j],linestyle='None',color=hex_colors[j])

            # Add labels and title
            plt.xlabel('Re[Z](Ohm)')
            plt.ylabel('-Im[Z](Ohm)')
            plt.title('Nyquist Impedance')
            #plt.xlim(100,1200000)       # X-axis from  to 
            #plt.ylim(10,1000000)  # Y-axis from  to 

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
        plt.show()
    
def density_plot():    
    #########################################
    # Density plot
    #########################################
    fig5, ax = plt.subplots(figsize=(8, 8))
    data4 = np.loadtxt('DATA/DENSIDADE.txt',skiprows=1)
    column1 = data4[:,0]
    column2 = data4[:,1]
    column3 = data4[:,2]
    column4 = data4[:,3]
   
    # Create plot
    ax.errorbar(column2,column3,column4, label='Density measurements', marker='o',linestyle='None',color=hex_colors[2],ecolor = 'black',capsize=5)
    
    mean = np.mean(column3)
    sigma = np.sqrt( (1.0/8.0)**2 * (column4[0]**2 + column4[1]**2 + column4[2]**2 + column4[3]**2 + column4[4]**2
                                   + column4[5]**2 + column4[6]**2 + column4[7]**2 ) )
    
    print("Mean: ",np.mean(column3))
    print("Average: ", np.average(column3))
    print("Median: ", np.median(column3))
    print("Sigma:" ,sigma)

    x = [0., 200]
    CeO_density = [mean, mean]
    ax.plot(x, CeO_density, linestyle='--',color='navy', label='Average value')
    ax.fill_between(x, mean - sigma, mean + sigma, alpha=0.2)
    
    # Add labels and title
    plt.xlabel('Compaction Pressure(MPa)')
    plt.ylabel('Density(g/cm^3)')
    plt.title('')
    plt.xlim(20,160) # X-axis from  to 
    plt.ylim(6.2,7.8)  # Y-axis from  to 

    # Scientific notation on both axes
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)

    # Add grid, minor ticks, and legend
    ax.grid(True, which='major', linestyle='-', alpha=0.3)
    ax.minorticks_on()
    ax.grid(True, which='minor', linestyle=':', alpha=0.2)
    #ax.legend(loc='upper right',frameon=False)
    
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [1, 0]
    ax.legend([handles[i] for i in order], [labels[i] for i in order])

    # Show the plot
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    # Set font to sans-serif for a scientific look
    plt.rcParams.update({
        'font.family': 'sans-serif',
        'font.size': 14,
        'axes.labelsize': 14,
        'axes.titlesize': 16,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'legend.fontsize': 14,
        'lines.linewidth': 1.5,
        'lines.markersize': 5,
        'mathtext.fontset': 'cm',
    })
    
    #QA_plot()
    #nyquist_plot_all()
    #nyquist_plot_by_temperature()
    density_plot()
