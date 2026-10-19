# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se analizaron los reportes semanales de ventas de RetailAndina S.A. en formatos CSV, JSON y Excel utilizando Python y R. Se comprobó que los tres archivos presentaron cinco filas y cuatro columnas, con los mismos registros observados. El ticket promedio general fue de $38,07 y la región Sierra registró las mayores ventas, con $30860. Se recomienda verificar la consistencia de los datos y estandarizar los reportes para facilitar futuros análisis.

## 1. ¿Los tres formatos contienen la misma información?

Al leer los archivos en Python y R, comprobé que los tres formatos presentaron las mismas dimensiones y los mismos registros al revisar su contenido.

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5|4 |pd.read_csv() / read_csv() |
| JSON | API de fidelización |5 |4 |json.load() + pd.json_normalize() / fromJSON() |
| Excel | Consolidado de finanzas | 5|4 |pd.read_excel() / read_excel() |

¿la estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?*
Aunque los formatos almacenan la información de distintas maneras, esto no modifica  su contenido. CSV organiza los datos como texto delimitado, JSON utiliza estructuras como listas y objetos, y Excel almacena la información en un archivo de libro de cálculo. En esta práctica, los registros observados coincidieron en los tres formatos.

## 2. Tipos de datos y calidad

Al inspeccionar los archivos, identifiqué los siguientes tipos de datos:

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` |int64 |int, num |Valores numéricos utilizados para calcular ventas e indicadores.|
| `clientes` |int64 |int, num |Cantidad de clientes de cada sucursal. |
| `sucursal` |object | chr| Texto que identifica cada sucursal.|
| `region` |object |chr | Texto que identifica la región correspondiente.|

*¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?*
Texto que identifica la región correspondiente.

Si la columna ventas se hubiera identificado como texto, podría indicar la presencia de símbolos, caracteres no numéricos o problemas de formato, lo que dificultaría la realización de cálculos.
## 3. Particularidades técnicas encontradas

CSV: Fue posible leer los datos directamente como una tabla mediante pd.read_csv() en Python y read_csv() en R. Las columnas numéricas y de texto se identificaron correctamente.

JSON: En Python, json.load() permitió cargar los registros y pd.json_normalize() organizarlos en un DataFrame. En R, utilicé fromJSON() y convertí el resultado a un data.frame.

Excel: Fue necesario indicar la hoja ventas mediante sheet_name en Python y sheet en R para seleccionar los datos correspondientes.
## 4. Indicadores para la reunión del lunes

Calculé los indicadores a partir del archivo CSV utilizando funciones de agrupación y operaciones matemáticas en Python y R.
| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | Quito Norte: $12.450; Quito Sur: $9.870; Guayaquil Centro: $15.200; Guayaquil Norte: $13.980; Cuenca: $8.540 |
| Ticket promedio (ventas ÷ clientes) |$38,07|
| Sucursal con mayor venta |Guayaquil Centro: $15.200 |
| Sucursal con menor venta |Cuenca: $8.540 |
| Región con mayor venta total |Sierra: $30.860 |

## 5. Conclusiones y recomendación

1 Los archivos CSV, JSON y Excel presentaron cinco filas y cuatro columnas, y sus registros observados coincidieron. Esto permitió trabajar con la información en Python y R a pesar de las diferencias entre formatos.

2 Las variables de ventas y clientes se identificaron como numéricas, lo que facilitó la creación de la columna ticket y el cálculo de los indicadores. Se obtuvo un ticket promedio general de $38,07.

3 Guayaquil Centro registró la mayor venta, con $15.200, mientras que Cuenca presentó la menor, con $8.540. Sierra fue la región con mayores ventas acumuladas, con $30.860. Estos resultados describen únicamente las cinco sucursales durante la semana analizada y no permiten proyectar ventas futuras.

Recomendación: Se recomienda a RetailAndina S.A. establecer un procedimiento de validación de los datos y estandarizar los formatos de los reportes para facilitar su integración y reducir posibles errores en futuros análisis.
