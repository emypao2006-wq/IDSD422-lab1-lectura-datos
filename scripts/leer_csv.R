install.packages("readr")
library(readr)
#Carga data/ventas.csv con readr::read_csv en un data.frame
ventas <- read_csv("data/ventas.csv")
#Imprime los primeros registros
head(ventas)
#Imprime las dimensiones
dim(ventas)
#Imprime el tipo de dato
str(ventas)

