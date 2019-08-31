"""Diccionarios son estructuras de datps consistentes en listas de pares
de variaables. Cada par tiene un elemento llamado key que puede ser de cualquier
tipo y otro elemento llamado valor que tambien puede ser de cualquier tipo
"""

edades = {"david":30, "victor":40, "crespo":50, "allen":21, "kike":22, "ana":23}
print(edades)
print(edades["david"]) #muestra el valor de la key
edades["victor"] = 100
print(edades)

for i in edades:
    print(i,edades[i])
