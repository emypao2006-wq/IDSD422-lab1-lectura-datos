install.packages("jsonlite")
library(jsonlite)
#Carga data/ventas.json con jsonlite::fromJSON
ventas <- fromJSON("data/ventas.json")
#Convertir el resultado en data.frame si hace falta
ventas <- as.data.frame(ventas)
#Imprime los primeros registros
head(ventas)
#Imprime las dimensiones
dim(ventas)
#Imprime el tipo de dato
str(ventas)