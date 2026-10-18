import pandas as pd
#Carga data/ventas.csv
ventas = pd.read_csv("data/ventas.csv")
#Imprime los tipos de cada columna
print("\n Tipos de datos:")
print(ventas.dtypes)
#Crea la columna derivada "ticket" = ventas / clientes
ventas["ticket"] = ventas["ventas"]/ventas["clientes"]
#Imprime las primeras filas con ticket
print("\n Primeras filas con ticket:")
print(ventas.head())
#Venta promedio por sucursal
print("\n Venta promedio por sucursal:")
print(ventas.groupby("sucursal")["ventas"].mean())
# Ticket promedio general
print("\n Ticket promedio general:")
print(ventas["ventas"].sum() / ventas["clientes"].sum())
# Sucursal con mayor venta
print("\n Sucursal con mayor venta:")
print(ventas["ventas"].max())
print("Sucursal con mayor venta:",
      ventas.loc[ventas["ventas"].idxmax(), "sucursal"])
# Sucursal con menor venta
print("\n Sucursal con menor venta:")
print(ventas["ventas"].min())
print("Sucursal con menor venta:",
      ventas.loc[ventas["ventas"].idxmin(), "sucursal"])
# Región con mayor venta total
print("\n Ventas por región:")
ventas_per_region = ventas.groupby("region")["ventas"].sum()
print(ventas_per_region.head())
print("\n Región con mayor venta")
print(ventas_per_region.idxmax())

