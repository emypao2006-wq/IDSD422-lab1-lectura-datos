install.packages("readr")
library(readr)
#Cargar el archivo CSV
ventas <- read_csv("data/ventas.csv")
#Imprime el tipos de dato
str(ventas)
#Verificar el tipo de dato de region
class(ventas$region)
#Crear la columna ticket = ventas / clientes
ventas$ticket <- ventas$ventas / ventas$clientes
#Imprime los primeros registros
head(ventas)
# Venta promedio por sucursal
promedio_sucursal <- aggregate(ventas ~ sucursal,
                              data = ventas, FUN = mean)
promedio_sucursal
# Ticket promedio general
ticket_promedio <- sum(ventas$ventas) / sum(ventas$clientes)
ticket_promedio
# Ventas totales por sucursal
ventas_sucursal <- aggregate(ventas ~ sucursal,
                            data = ventas, FUN = sum)
ventas_sucursal
# Sucursal con mayor venta
max(ventas_sucursal$ventas)
ventas_sucursal$sucursal[
  which.max(ventas_sucursal$ventas)
]
# Sucursal con menor venta
min(ventas_sucursal$ventas)
ventas_sucursal$sucursal[
  which.min(ventas_sucursal$ventas)
]
# Region con mayor venta total
ventas_region <- aggregate(ventas ~ region,
                          data = ventas, FUN = sum)
ventas_region
ventas_region$region[
  which.max(ventas_region$ventas)
]
