import pandas as pd
#Lee el archivo CSV
ventas = pd.read_csv("/content/data/ventas.csv")
#Imprime los primeros registros
print(ventas.head())
#Imprime las dimensiones
print("Dimensiones:", ventas.shape)
#Imprime los tipos de datos
print(ventas.dtypes)