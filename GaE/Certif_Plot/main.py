import pandas as pd
from my_lib import print_page
from matplotlib.backends.backend_pdf import PdfPages

# reading the txt file which should be placed in the same directory as main.py

data = pd.read_csv(r'zynqAdcLog.txt', header=0, delimiter=',',
                   usecols=[0,3,10,11], low_memory=False) #read specific columns from txt file

sample = data.iloc[:,0]   # Read sample colummn
name = data.iloc[:,1]     # Read name colummn
cur_phy = data.iloc[:,2]  # Read cur_phy column
rms = data.iloc[:,3]      # Read rms column

name_lst = list(name)     # create a list with all variables
name_length = len(name)   # calc how many var has been sampled

with PdfPages(r'Charts.pdf') as export_pdf:
    # Page 1
    print_page('UDC_A','UDC2_A','UDC3_A',
                name,name_length,sample,rms,cur_phy,export_pdf)
    print("Page1 done")
    # Page 2
    print_page('UDC_GRID1', 'UDC_GRID2', 'UDC_GENA1',
               name, name_length, sample, rms, cur_phy, export_pdf)
    print("Page2 done")
    # Page 3
    print_page('UDC_GENA2', 'UDC_GENB1', 'UDC_GENB2',
               name, name_length, sample, rms, cur_phy, export_pdf)
    print("Page3 done")
    #Page 4
    print_page('I_GRID1_A', 'I_GRID2_A', 'I_GRID3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page4 done")
    # Page 5
    print_page('I_GENA1_A', 'I_GENA2_A', 'I_GENA3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page5 done")
    #Page 6
    print_page('I_GENB1_A', 'I_GENB2_A', 'I_GENB3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page6 done")
    # Page 7
    print_page('T_GRID1_A', 'T_GRID2_A', 'T_GRID3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page7 done")
    #Page 8
    print_page('T_GENA1_A', 'T_GENA2_A', 'T_GENA3_A',
               name, name_length, sample, rms, cur_phy, export_pdf)
    print("Page8 done")
    # Page 9
    print_page('T_GENB1_A', 'T_GENB2_A', 'T_GENB3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page9 done")
    #Page 10
    print_page('Temp.1', 'Temp.2', 'Temp.3',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page10 done")
    # Page 11
    print_page('Temp.4', 'Temp.5', 'Temp.6',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page11 done")
    # Page 12
    print_page('Temp.7', 'Temp.8', 'Temp.9',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page12 done")
    # Page 13
    print_page('Temp.10', 'PT100_AUX1', 'PT100_AUX2',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page13 done")
    #Page 14
    print_page('PT100_AUX3', 'PT100_AUX4', 'PT100_AUX5',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page14 done")
    # Page 15
    print_page('PT100_AUX6', 'AUXADAPT_IN_1', 'AUXADAPT_IN_2',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page15 done")
    # Page 16
    print_page('T_Chip', 'VANA_monit', '-Vana_monit',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page16 done")
    # Page 17
    print_page('Vana_T_monit', '4_5Vref_monit', '5VADC_monit',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page17 done")
    # Page 18
    print_page('24V_BOARD_monit', '24V_I/O_monit', '24V_BOARD_current',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page18 done")
    # Page 19
    print_page('24V_I/O_current', '24V_skgrid_current', '24V_skgen_current',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page19 done")
    # Page 20
    print_page('ILA_1_A', 'ILA_2_A', 'ILA_3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page20 done")
    # Page 21
    print_page('ILB_1_A', 'ILB_2_A', 'ILB_3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page21 done")
    # Page 22
    print_page('UL1_A', 'UL2_A', 'UL3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page22 done")
    # Page 23
    print_page('UGEN1_A', 'UGEN2_A', 'UGEN3_A',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page23 done")
    # Page 24
    print_page('T_BOARD', '24V_SKIIP_monit', ' ',
               name, name_length, sample, rms,cur_phy,export_pdf)
    print("Page24 done")