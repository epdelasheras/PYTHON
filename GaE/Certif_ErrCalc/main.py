import os
import pandas as pd
from my_lib import data_filter

# Variable para la ruta al directorio
path = './CCU'

# Lista vacia para incluir los ficheros
lstFiles = []

# Lista con todos los ficheros del directorio:
lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros

# Crea una lista de los ficheros txt que existen en el directorio y los incluye a la lista.

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".txt"):
            lstFiles.append(nombreFichero + extension)
            # print (nombreFichero+extension)

print(lstFiles)
print('LISTADO FINALIZADO')
print("longitud de la lista = ", len(lstFiles))


# Deleting zynqlog from the list
lstPosition = [i for i, s in enumerate(lstFiles) if 'zynqLog' in s]
lstFiles.remove(lstFiles[lstPosition[0]])

print(lstFiles)


# opening all the files
data = pd.read_csv("./CCU/"+lstFiles[0], header=0, delimiter=',',
                   usecols=[0,3,10,11], low_memory=False) #read specific columns from txt file

sample = data.iloc[:,0]   # Read sample colummn
name = data.iloc[:,1]     # Read name colummn
cur_phy = data.iloc[:,2]  # Read cur_phy column
rms = data.iloc[:,3]      # Read rms column

name_lst = list(name)     # create a list with all variables
name_length = len(name)   # calc how many var has been sampled

sample_lst, cur_phy_lst, rms_lst = data_filter(name,name_length,'UDC2_A',sample,cur_phy,rms)

print (cur_phy_lst)
