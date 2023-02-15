#Importar pandas
import pandas as pd
fuenteDato=pd.read_csv("./empleados.csv")

#1. Filtrar empleados que solo sean analistas 1
analista1=fuenteDato[fuenteDato["cargo"]=="analista1"]
print(analista1)

#2. Filtrar empleados que solo sean analistas 2
analista2=fuenteDato[fuenteDato["cargo"]=="analista2"]
print(analista2)

#3. Filtrar empleados en general que tengan menos de 30 años
menores30=fuenteDato[fuenteDato["edad"]<30]
print(menores30)

#4. Filtrar empleados en general que tengan mas de 50 años
mayor50=fuenteDato[fuenteDato["edad"]>50]
print(mayor50)

#5. ¿Cuál es el promedio de salario de un analista 1?
promedioAnalista1=analista1[["salario"]].mean()
print(round(promedioAnalista1,2))

#6. ¿Cuál es el promedio de salario de un analista 2?
promedioAnalista2=analista2[["salario"]].mean()
print(round(promedioAnalista2,2))

#7. Filtrar empleados cuto porcentaje de deducción sea mayor al 10%
filtro7=fuenteDato[fuenteDato["porcentajeDeduccion"]>10]
print(filtro7)

#8. Cambiar todos los datos nan por el valor 0

#9. Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0
