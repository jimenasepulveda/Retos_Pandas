import pandas as pd 
fuenteDato=pd.read_csv("./exterior.csv")

#1. Puedo mostrar todos los datos de la columna Área Conocimiento?
filtro=fuenteDato["Área Conocimiento"].to_string()
print(filtro)

#2. Filtrar los primeros 20 registros
filtro1=fuenteDato.head(20)
print(filtro1)

#3. Filtrar los últimos 35 registros
filtro2=fuenteDato.tail(35)
print(filtro2)

#4. Es posible obtener solo la fila de medias
medias=fuenteDato.loc[['mean']]
print("\n")
mediaEdad=medias["edad"]
print(mediaEdad)