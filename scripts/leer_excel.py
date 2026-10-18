import pandas as pd
#Lee la hoja de Excel
ventas = pd.read_excel("/content/data/ventas.xlsx", sheet_name="ventas")
#Imprime los primeros registros
print(ventas.head())
#Imprime las dimensiones
print("Dimensiones:", ventas.shape)
#Imprime los tipos de datos
print("\nTipos de columna")
print(ventas.dtypes)