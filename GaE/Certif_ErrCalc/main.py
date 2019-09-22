import os
import pandas as pd
from my_lib import calc_sample
from my_lib import data_filter
from my_lib import error_absolute
from my_lib import error_relative

print('Creando lista con los nombres de los txt a procesar')

# Path of the txt files to read
path = './CCU'

# Empty list to include all the txt file names
lstFiles = []

# List with all the files of the folder
lstDir = os.walk(path)

# Create a list with txt files of the folder and included in the list
for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".txt"):
            lstFiles.append("./CCU/" + nombreFichero + extension)

# Deleting zynqlog from the list
lstPosition = [i for i, s in enumerate(lstFiles) if 'zynqLog' in s]
lstFiles.remove(lstFiles[lstPosition[0]])

print("Creando fichero unico ZynqAdcFinal.txt")
# Joining all the logs together in one file.
with open('ZynqAdcFinal.txt', 'w') as outfile:
    for fname in lstFiles:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

print("Leyendo información de interés de ZybqAdcFinal.txt")
# Reading only the data which is going to be processed
data = pd.read_csv("ZynqAdcFinal.txt", header=0, delimiter=',',
                   usecols=[0, 3, 10, 11], low_memory=False)  # read specific columns from txt file
sample = data.iloc[:, 0]  # Read sample colummn
name = data.iloc[:, 1]  # Read name colummn
cur_phy = data.iloc[:, 2]  # Read cur_phy column
rms = data.iloc[:, 3]  # Read rms column


name_lst = list(name)     # create a list with all variables
name_length = len(name)   # calc how many var has been sampled

sample_lst = calc_sample(name,name_length,'UDC2_A',sample)
print("Se van a procesar un total de: ", len(sample_lst), "muestras")

'''*************UDC channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida de UDC")
UDC_A_cur_phy_lst, UDC_A_rms_lst = data_filter(name,name_length,'UDC_A',cur_phy,rms)
UDC2_A_cur_phy_lst, UDC2_A_rms_lst = data_filter(name,name_length,'UDC2_A',cur_phy,rms)
UDC3_A_cur_phy_lst, UDC3_A_rms_lst = data_filter(name,name_length,'UDC3_A',cur_phy,rms)
UDC_GRID1_cur_phy_lst, UDC_GRID1_rms_lst = data_filter(name,name_length,'UDC_GRID1',cur_phy,rms)
UDC_GRID2_cur_phy_lst, UDC_GRID2_rms_lst = data_filter(name,name_length,'UDC_GRID2',cur_phy,rms)
UDC_GENA1_cur_phy_lst, UDC_GENA1_rms_lst = data_filter(name,name_length,'UDC_GENA1',cur_phy,rms)
UDC_GENA2_cur_phy_lst, UDC_GENA2_rms_lst = data_filter(name,name_length,'UDC_GENA2',cur_phy,rms)
UDC_GENB1_cur_phy_lst, UDC_GENB1_rms_lst = data_filter(name,name_length,'UDC_GENB1',cur_phy,rms)
UDC_GENB2_cur_phy_lst, UDC_GENB2_rms_lst = data_filter(name,name_length,'UDC_GENB2',cur_phy,rms)

real_value = 4.9955

UDC_A_ea_mean = error_absolute(UDC_A_cur_phy_lst, real_value)
UDC_A_er_percent = error_relative(UDC_A_ea_mean, real_value)

UDC2_A_ea_mean = error_absolute(UDC2_A_cur_phy_lst, real_value)
UDC2_A_er_percent = error_relative(UDC_A_ea_mean, real_value)

UDC3_A_ea_mean = error_absolute(UDC3_A_cur_phy_lst, real_value)
UDC3_A_er_percent = error_relative(UDC3_A_ea_mean, real_value)

UDC_GRID2_ea_mean = error_absolute(UDC_GRID2_cur_phy_lst, real_value)
UDC_GRID2_er_percent = error_relative(UDC_GRID2_ea_mean, real_value)

UDC_GENA1_ea_mean = error_absolute(UDC_GENA1_cur_phy_lst, real_value)
UDC_GENA1_er_percent = error_relative(UDC_GENA1_ea_mean, real_value)

UDC_GENA2_ea_mean = error_absolute(UDC_GENA2_cur_phy_lst, real_value)
UDC_GENA2_er_percent = error_relative(UDC_GENA2_ea_mean, real_value)

UDC_GENB1_ea_mean = error_absolute(UDC_GENB1_cur_phy_lst, real_value)
UDC_GENB1_er_percent = error_relative(UDC_GENB1_ea_mean, real_value)

UDC_GENB2_ea_mean = error_absolute(UDC_GENB2_cur_phy_lst, real_value)
UDC_GENB2_er_percent = error_relative(UDC_GENB2_ea_mean, real_value)


UDC_ea_average = (UDC_A_ea_mean + UDC2_A_ea_mean + UDC3_A_ea_mean +
                 UDC_GRID2_ea_mean + UDC_GENA1_ea_mean +
                 UDC_GENA2_ea_mean + UDC_GENB1_ea_mean + UDC_GENB2_ea_mean)/8

UDC_er_percent = (UDC_A_er_percent + UDC2_A_er_percent + UDC3_A_er_percent +
                 UDC_GRID2_er_percent + UDC_GENA1_er_percent +
                 UDC_GENA2_er_percent + UDC_GENB1_er_percent + UDC_GENB2_er_percent)/8

print("El error absoluto medio de todas las medidas de UDC es (V): ",UDC_ea_average)
print("El error relativo medio de todas las medidas de UDC es (%): ",UDC_er_percent)

'''*************I_SKiiP channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida I_SkiiP")
real_value = 4.995
I_GRID1_A_cur_phy_lst, I_GRID1_A_rms_lst = data_filter(name,name_length,'I_GRID1_A',cur_phy,rms)
I_GRID1_A_ea_mean = error_absolute(I_GRID1_A_cur_phy_lst, real_value)
I_GRID1_A_er_percent = error_relative(I_GRID1_A_ea_mean, real_value)

I_GRID2_A_cur_phy_lst, I_GRID2_A_rms_lst = data_filter(name,name_length,'I_GRID2_A',cur_phy,rms)
I_GRID2_A_ea_mean = error_absolute(I_GRID2_A_cur_phy_lst, real_value)
I_GRID2_A_er_percent = error_relative(I_GRID2_A_ea_mean, real_value)

I_GRID3_A_cur_phy_lst, I_GRID3_A_rms_lst = data_filter(name,name_length,'I_GRID3_A',cur_phy,rms)
I_GRID3_A_ea_mean = error_absolute(I_GRID3_A_cur_phy_lst, real_value)
I_GRID3_A_er_percent = error_relative(I_GRID3_A_ea_mean, real_value)

I_GENA1_A_cur_phy_lst, I_GENA1_A_rms_lst = data_filter(name,name_length,'I_GENA1_A',cur_phy,rms)
I_GENA1_A_ea_mean = error_absolute(I_GENA1_A_cur_phy_lst, real_value)
I_GENA1_A_er_percent = error_relative(I_GENA1_A_ea_mean, real_value)

I_GENA2_A_cur_phy_lst, I_GENA2_A_rms_lst = data_filter(name,name_length,'I_GENA2_A',cur_phy,rms)
I_GENA2_A_ea_mean = error_absolute(I_GENA2_A_cur_phy_lst, real_value)
I_GENA2_A_er_percent = error_relative(I_GENA2_A_ea_mean, real_value)

I_GENA3_A_cur_phy_lst, I_GENA3_A_rms_lst = data_filter(name,name_length,'I_GENA3_A',cur_phy,rms)
I_GENA3_A_ea_mean = error_absolute(I_GENA3_A_cur_phy_lst, real_value)
I_GENA3_A_er_percent = error_relative(I_GENA3_A_ea_mean, real_value)

I_GENB1_A_cur_phy_lst, I_GENB1_A_rms_lst = data_filter(name,name_length,'I_GENB1_A',cur_phy,rms)
I_GENB1_A_ea_mean = error_absolute(I_GENB1_A_cur_phy_lst, real_value)
I_GENB1_A_er_percent = error_relative(I_GENB1_A_ea_mean, real_value)

I_GENB2_A_cur_phy_lst, I_GENB2_A_rms_lst = data_filter(name,name_length,'I_GENB2_A',cur_phy,rms)
I_GENB2_A_ea_mean = error_absolute(I_GENB2_A_cur_phy_lst, real_value)
I_GENB2_A_er_percent = error_relative(I_GENB2_A_ea_mean, real_value)

I_GENB3_A_cur_phy_lst, I_GENB3_A_rms_lst = data_filter(name,name_length,'I_GENB3_A',cur_phy,rms)
I_GENB3_A_ea_mean = error_absolute(I_GENB3_A_cur_phy_lst, real_value)
I_GENB3_A_er_percent = error_relative(I_GENB3_A_ea_mean, real_value)

I_SKIIP_ea_average = (I_GRID1_A_ea_mean + I_GRID2_A_ea_mean + I_GRID3_A_ea_mean +
                      I_GENA1_A_ea_mean + I_GENA2_A_ea_mean + I_GENA3_A_ea_mean +
                      I_GENB1_A_ea_mean + I_GENB2_A_ea_mean + I_GENB3_A_ea_mean)/9

I_SKIIP_er_percent = (I_GRID1_A_er_percent + I_GRID2_A_er_percent + I_GRID3_A_er_percent +
                      I_GENA1_A_er_percent + I_GENA2_A_er_percent + I_GENA3_A_er_percent +
                      I_GENB1_A_er_percent + I_GENB2_A_er_percent + I_GENB3_A_er_percent)/9

print("El error absoluto medio de todas las medidas de I_SKiiP es (V): ",I_SKIIP_ea_average)
print("El error relativo medio de todas las medidas de I_SKiiP es (%): ",I_SKIIP_er_percent)

'''*************T_SKiiP channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida T_SkiiP")
real_value = 4.975
T_GRID1_A_cur_phy_lst, T_GRID1_A_rms_lst = data_filter(name,name_length,'T_GRID1_A',cur_phy,rms)
T_GRID1_A_ea_mean = error_absolute(T_GRID1_A_cur_phy_lst, real_value)
T_GRID1_A_er_percent = error_relative(T_GRID1_A_ea_mean, real_value)

T_GRID2_A_cur_phy_lst, T_GRID2_A_rms_lst = data_filter(name,name_length,'T_GRID2_A',cur_phy,rms)
T_GRID2_A_ea_mean = error_absolute(T_GRID2_A_cur_phy_lst, real_value)
T_GRID2_A_er_percent = error_relative(T_GRID2_A_ea_mean, real_value)

T_GRID3_A_cur_phy_lst, T_GRID3_A_rms_lst = data_filter(name,name_length,'T_GRID3_A',cur_phy,rms)
T_GRID3_A_ea_mean = error_absolute(T_GRID3_A_cur_phy_lst, real_value)
T_GRID3_A_er_percent = error_relative(T_GRID3_A_ea_mean, real_value)

T_GENA1_A_cur_phy_lst, T_GENA1_A_rms_lst = data_filter(name,name_length,'T_GENA1_A',cur_phy,rms)
T_GENA1_A_ea_mean = error_absolute(T_GENA1_A_cur_phy_lst, real_value)
T_GENA1_A_er_percent = error_relative(T_GENA1_A_ea_mean, real_value)

T_GENA2_A_cur_phy_lst, T_GENA2_A_rms_lst = data_filter(name,name_length,'T_GENA2_A',cur_phy,rms)
T_GENA2_A_ea_mean = error_absolute(T_GENA2_A_cur_phy_lst, real_value)
T_GENA2_A_er_percent = error_relative(T_GENA2_A_ea_mean, real_value)

T_GENA3_A_cur_phy_lst, T_GENA3_A_rms_lst = data_filter(name,name_length,'T_GENA3_A',cur_phy,rms)
T_GENA3_A_ea_mean = error_absolute(T_GENA3_A_cur_phy_lst, real_value)
T_GENA3_A_er_percent = error_relative(T_GENA3_A_ea_mean, real_value)

T_GENB1_A_cur_phy_lst, T_GENB1_A_rms_lst = data_filter(name,name_length,'T_GENB1_A',cur_phy,rms)
T_GENB1_A_ea_mean = error_absolute(T_GENB1_A_cur_phy_lst, real_value)
T_GENB1_A_er_percent = error_relative(T_GENB1_A_ea_mean, real_value)

T_GENB2_A_cur_phy_lst, T_GENB2_A_rms_lst = data_filter(name,name_length,'T_GENB2_A',cur_phy,rms)
T_GENB2_A_ea_mean = error_absolute(T_GENB2_A_cur_phy_lst, real_value)
T_GENB2_A_er_percent = error_relative(T_GENB2_A_ea_mean, real_value)

T_GENB3_A_cur_phy_lst, T_GENB3_A_rms_lst = data_filter(name,name_length,'T_GENB3_A',cur_phy,rms)
T_GENB3_A_ea_mean = error_absolute(T_GENB3_A_cur_phy_lst, real_value)
T_GENB3_A_er_percent = error_relative(T_GENB3_A_ea_mean, real_value)

T_SKIIP_ea_average = (T_GRID1_A_ea_mean + T_GRID2_A_ea_mean + T_GRID3_A_ea_mean +
                      T_GENA1_A_ea_mean + T_GENA2_A_ea_mean + T_GENA3_A_ea_mean +
                      T_GENB1_A_ea_mean + T_GENB2_A_ea_mean + T_GENB3_A_ea_mean)/9

T_SKIIP_er_percent = (T_GRID1_A_er_percent + T_GRID2_A_er_percent + T_GRID3_A_er_percent +
                      T_GENA1_A_er_percent + T_GENA2_A_er_percent + T_GENA3_A_er_percent +
                      T_GENB1_A_er_percent + T_GENB2_A_er_percent + T_GENB3_A_er_percent)/9

print("El error absoluto medio de todas las medidas de T_SKiiP es (V): ",T_SKIIP_ea_average)
print("El error relativo medio de todas las medidas de T_SKiiP es (%): ",T_SKIIP_er_percent)

'''*************PT100 channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida PT100")
real_value = 115
Temp1_cur_phy_lst, Temp1_rms_lst = data_filter(name,name_length,'Temp.1',cur_phy,rms)
Temp1_ea_mean = error_absolute(Temp1_cur_phy_lst, real_value)
Temp1_er_percent = error_relative(Temp1_ea_mean, real_value)

Temp2_cur_phy_lst, Temp2_rms_lst = data_filter(name,name_length,'Temp.2',cur_phy,rms)
Temp2_ea_mean = error_absolute(Temp2_cur_phy_lst, real_value)
Temp2_er_percent = error_relative(Temp2_ea_mean, real_value)

Temp3_cur_phy_lst, Temp3_rms_lst = data_filter(name,name_length,'Temp.3',cur_phy,rms)
Temp3_ea_mean = error_absolute(Temp3_cur_phy_lst, real_value)
Temp3_er_percent = error_relative(Temp3_ea_mean, real_value)

Temp4_cur_phy_lst, Temp4_rms_lst = data_filter(name,name_length,'Temp.4',cur_phy,rms)
Temp4_ea_mean = error_absolute(Temp4_cur_phy_lst, real_value)
Temp4_er_percent = error_relative(Temp4_ea_mean, real_value)

Temp5_cur_phy_lst, Temp5_rms_lst = data_filter(name,name_length,'Temp.5',cur_phy,rms)
Temp5_ea_mean = error_absolute(Temp5_cur_phy_lst, real_value)
Temp5_er_percent = error_relative(Temp5_ea_mean, real_value)

Temp6_cur_phy_lst, Temp6_rms_lst = data_filter(name,name_length,'Temp.6',cur_phy,rms)
Temp6_ea_mean = error_absolute(Temp6_cur_phy_lst, real_value)
Temp6_er_percent = error_relative(Temp6_ea_mean, real_value)

Temp7_cur_phy_lst, Temp7_rms_lst = data_filter(name,name_length,'Temp.7',cur_phy,rms)
Temp7_ea_mean = error_absolute(Temp7_cur_phy_lst, real_value)
Temp7_er_percent = error_relative(Temp7_ea_mean, real_value)

Temp8_cur_phy_lst, Temp8_rms_lst = data_filter(name,name_length,'Temp.8',cur_phy,rms)
Temp8_ea_mean = error_absolute(Temp8_cur_phy_lst, real_value)
Temp8_er_percent = error_relative(Temp8_ea_mean, real_value)

Temp9_cur_phy_lst, Temp9_rms_lst = data_filter(name,name_length,'Temp.9',cur_phy,rms)
Temp9_ea_mean = error_absolute(Temp9_cur_phy_lst, real_value)
Temp9_er_percent = error_relative(Temp9_ea_mean, real_value)

Temp10_cur_phy_lst, Temp10_rms_lst = data_filter(name,name_length,'Temp.10',cur_phy,rms)
Temp10_ea_mean = error_absolute(Temp10_cur_phy_lst, real_value)
Temp10_er_percent = error_relative(Temp10_ea_mean, real_value)

PT100_AUX1_cur_phy_lst, PT100_AUX1_rms_lst = data_filter(name,name_length,'PT100_AUX1',cur_phy,rms)
PT100_AUX1_ea_mean = error_absolute(PT100_AUX1_cur_phy_lst, real_value)
PT100_AUX1_er_percent = error_relative(PT100_AUX1_ea_mean, real_value)

PT100_AUX2_cur_phy_lst, PT100_AUX2_rms_lst = data_filter(name,name_length,'PT100_AUX2',cur_phy,rms)
PT100_AUX2_ea_mean = error_absolute(PT100_AUX2_cur_phy_lst, real_value)
PT100_AUX2_er_percent = error_relative(PT100_AUX2_ea_mean, real_value)

PT100_AUX3_cur_phy_lst, PT100_AUX3_rms_lst = data_filter(name,name_length,'PT100_AUX3',cur_phy,rms)
PT100_AUX3_ea_mean = error_absolute(PT100_AUX3_cur_phy_lst, real_value)
PT100_AUX3_er_percent = error_relative(PT100_AUX3_ea_mean, real_value)

PT100_AUX4_cur_phy_lst, PT100_AUX4_rms_lst = data_filter(name,name_length,'PT100_AUX4',cur_phy,rms)
PT100_AUX4_ea_mean = error_absolute(PT100_AUX4_cur_phy_lst, real_value)
PT100_AUX4_er_percent = error_relative(PT100_AUX4_ea_mean, real_value)

PT100_AUX5_cur_phy_lst, PT100_AUX5_rms_lst = data_filter(name,name_length,'PT100_AUX5',cur_phy,rms)
PT100_AUX5_ea_mean = error_absolute(PT100_AUX5_cur_phy_lst, real_value)
PT100_AUX5_er_percent = error_relative(PT100_AUX5_ea_mean, real_value)

PT100_ea_average = (Temp1_ea_mean + Temp2_ea_mean + Temp3_ea_mean + Temp4_ea_mean +
                    Temp5_ea_mean + Temp6_ea_mean + Temp7_ea_mean + Temp8_ea_mean +
                    Temp9_ea_mean + Temp10_ea_mean + PT100_AUX1_ea_mean + PT100_AUX2_ea_mean +
                    PT100_AUX3_ea_mean + PT100_AUX4_ea_mean + PT100_AUX5_ea_mean)/15

PT100_er_percent = (Temp1_er_percent + Temp2_er_percent + Temp3_er_percent + Temp4_er_percent +
                    Temp5_er_percent + Temp6_er_percent + Temp7_er_percent + Temp8_er_percent +
                    Temp9_er_percent + Temp10_er_percent + PT100_AUX1_er_percent +
                    PT100_AUX2_er_percent + PT100_AUX3_er_percent + PT100_AUX4_er_percent +
                    PT100_AUX5_er_percent)/15

print("El error absoluto medio de todas las medidas de PT100 es (Ohm): ",PT100_ea_average)
print("El error relativo medio de todas las medidas de PT100 es (%): ",PT100_er_percent)

'''*************ILA channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida ILA")
real_value = 38.0 # Not sure
ILA_1_A_cur_phy_lst, ILA_1_A_rms_lst = data_filter(name,name_length,'ILA_1_A',cur_phy,rms)
ILA_1_A_ea_mean = error_absolute(ILA_1_A_rms_lst, real_value)
ILA_1_A_er_percent = error_relative(ILA_1_A_ea_mean, real_value)

ILA_2_A_cur_phy_lst, ILA_2_A_rms_lst = data_filter(name,name_length,'ILA_2_A',cur_phy,rms)
ILA_2_A_ea_mean = error_absolute(ILA_2_A_rms_lst, real_value)
ILA_2_A_er_percent = error_relative(ILA_2_A_ea_mean, real_value)

ILA_3_A_cur_phy_lst, ILA_3_A_rms_lst = data_filter(name,name_length,'ILA_3_A',cur_phy,rms)
ILA_3_A_ea_mean = error_absolute(ILA_3_A_rms_lst, real_value)
ILA_3_A_er_percent = error_relative(ILA_3_A_ea_mean, real_value)

ILA_ea_average = (ILA_1_A_ea_mean + ILA_2_A_ea_mean + ILA_3_A_ea_mean)/3

ILA_er_percent = (ILA_1_A_er_percent + ILA_2_A_er_percent + ILA_3_A_er_percent)/3

print("El error absoluto medio de todas las medidas de ILA es (A): ",ILA_ea_average)
print("El error relativo medio de todas las medidas de ILA es (%): ",ILA_er_percent)

'''*************ILB channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medida ILB")
real_value = 42.0 # Not sure
ILB_1_A_cur_phy_lst, ILB_1_A_rms_lst = data_filter(name,name_length,'ILB_1_A',cur_phy,rms)
ILB_1_A_ea_mean = error_absolute(ILB_1_A_rms_lst, real_value)
ILB_1_A_er_percent = error_relative(ILB_1_A_ea_mean, real_value)

ILB_2_A_cur_phy_lst, ILB_2_A_rms_lst = data_filter(name,name_length,'ILB_2_A',cur_phy,rms)
ILB_2_A_ea_mean = error_absolute(ILB_2_A_rms_lst, real_value)
ILB_2_A_er_percent = error_relative(ILB_2_A_ea_mean, real_value)

ILB_3_A_cur_phy_lst, ILB_3_A_rms_lst = data_filter(name,name_length,'ILB_3_A',cur_phy,rms)
ILB_3_A_ea_mean = error_absolute(ILB_3_A_rms_lst, real_value)
ILB_3_A_er_percent = error_relative(ILB_3_A_ea_mean, real_value)

ILB_ea_average = (ILB_1_A_ea_mean + ILB_2_A_ea_mean + ILB_3_A_ea_mean)/3

ILB_er_percent = (ILB_1_A_er_percent + ILB_2_A_er_percent + ILB_3_A_er_percent)/3

print("El error absoluto medio de todas las medidas de ILB es (A): ",ILB_ea_average)
print("El error relativo medio de todas las medidas de ILB es (%): ",ILB_er_percent)

'''*************UL&UGEN channel => Averaging Ea & Er*******************'''
print("Procesando muestras de los canales de medidas UL & UGEN")
real_value = 223.0 # Not sure
UL1_A_cur_phy_lst, UL1_A_rms_lst = data_filter(name,name_length,'UL1_A',cur_phy,rms)
UL1_A_ea_mean = error_absolute(UL1_A_rms_lst, real_value)
UL1_A_er_percent = error_relative(UL1_A_ea_mean, real_value)

UL2_A_cur_phy_lst, UL2_A_rms_lst = data_filter(name,name_length,'UL2_A',cur_phy,rms)
UL2_A_ea_mean = error_absolute(UL2_A_rms_lst, real_value)
UL2_A_er_percent = error_relative(UL2_A_ea_mean, real_value)

UL3_A_cur_phy_lst, UL3_A_rms_lst = data_filter(name,name_length,'UL3_A',cur_phy,rms)
UL3_A_ea_mean = error_absolute(UL3_A_rms_lst, real_value)
UL3_A_er_percent = error_relative(UL3_A_ea_mean, real_value)

UGEN1_A_cur_phy_lst, UGEN1_A_rms_lst = data_filter(name,name_length,'UGEN1_A',cur_phy,rms)
UGEN1_A_ea_mean = error_absolute(UGEN1_A_rms_lst, real_value)
UGEN1_A_er_percent = error_relative(UGEN1_A_ea_mean, real_value)

UGEN2_A_cur_phy_lst, UGEN2_A_rms_lst = data_filter(name,name_length,'UGEN2_A',cur_phy,rms)
UGEN2_A_ea_mean = error_absolute(UGEN2_A_rms_lst, real_value)
UGEN2_A_er_percent = error_relative(UGEN2_A_ea_mean, real_value)

UGEN3_A_cur_phy_lst, UGEN3_A_rms_lst = data_filter(name,name_length,'UGEN3_A',cur_phy,rms)
UGEN3_A_ea_mean = error_absolute(UGEN3_A_rms_lst, real_value)
UGEN3_A_er_percent = error_relative(UGEN3_A_ea_mean, real_value)

UL_UGEN_ea_average = (UL1_A_ea_mean + UL2_A_ea_mean + UL3_A_ea_mean +
                      UGEN1_A_ea_mean + UGEN2_A_ea_mean + UGEN3_A_ea_mean)/6

UL_UGEN_er_percent = (UL1_A_er_percent + UL2_A_er_percent + UL2_A_er_percent +
                      UGEN1_A_er_percent + UGEN2_A_er_percent + UGEN3_A_er_percent)/6

print("El error absoluto medio de todas las medidas de UGEN_er_percent es (V): ",UL_UGEN_ea_average)
print("El error relativo medio de todas las medidas de UGEN_er_percent es (%): ",UL_UGEN_er_percent)

#Creando fichero de texto con los resultados
print("Creando fichero de resultados results.txt")
with open('results.txt', 'w') as resultfile:
    resultfile.write("************ACCURACY OF THE ANALOGIC CHANNELS OF THE CCU_SoC*************\n\n")
    resultfile.write("+UDC Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(UDC_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(UDC_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+I_SKiiP Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(I_SKIIP_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(I_SKIIP_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+T_SKiiP Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(T_SKIIP_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(T_SKIIP_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+T_SKiiP Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(PT100_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(PT100_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+ILA Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(ILA_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(ILA_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+ILB Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(ILB_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(ILB_er_percent))
    resultfile.write("\n\n")
    #
    resultfile.write("+UL&UGEN Channels:\n")
    resultfile.write(" - Absolute Error(V):")
    resultfile.write(str(UL_UGEN_ea_average))
    resultfile.write("\n")
    resultfile.write(" - Relative Error(%):")
    resultfile.write(str(UL_UGEN_er_percent))
    resultfile.write("\n\n")
