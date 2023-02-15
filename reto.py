import pandas as pd 
fuenteDato=pd.read_csv("./empleados.csv")

#primeros 50 con salario 
primeros50=fuenteDato.head(50)["salario"]
print("\n")
print(primeros50)

#obtener informacion general de los 500 registros encontrando la media aritmetica o promedio de salarios
media=fuenteDato.describe()
print("\n")
print(media)

#datos del registro 100,200,300,400
filtro=fuenteDato.iloc[[100,200,300,400]]
print("\n")
print(filtro)

#ultimos 3 empleados. solo quiero ver el nombre y el salario
nom_sal=fuenteDato.tail(3)[["nombres","salario"]]
print("\n")
print(nom_sal)