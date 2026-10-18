install.packages("readxl")
library(readxl)
#Carga data/ventas.xlsx con readxl::read_excel indicando la hoja
ventas <- read_excel("data/ventas.xlsx",sheet="ventas")
#Imprime los primeros registros                                                                                
head(ventas)
#Imprime las dimensiones
dim(ventas)
#Imprime el tipo de dato
str(ventas)