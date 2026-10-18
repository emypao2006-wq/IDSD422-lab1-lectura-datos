import json
import pandas as pd
#Lee el archivo JSON
with open("data/ventas.json", encoding="utf-8") as f:
  datos = json.load(f)
  #Convierte la estructura JSON en una tabla
  ventas = pd.json_normalize(datos)
#Imprime los primeros registros
print(ventas.head())
#Imprime las dimensiones
print("Dimensiones:", ventas.shape)
#Imprime tipos de datos
print("\nTipos de columna")
print(ventas.dtypes)