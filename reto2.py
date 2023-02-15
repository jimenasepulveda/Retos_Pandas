#1. Importo a pandas 
import pandas as pd

#2. Traigo la fuente de datos 
Nacional={84,88,84,87,80,83,84,90,78,82,84,90,75,78,98,100,78,65,80,20}
Medellín={90,78,68,87,102,90,80,80,81,78,79,81,83,84.5,90,101,60,70,80,87}

#3. Genero los dataframe 
dataframe1=pd.DataFrame(Nacional)
dataframe2=pd.DataFrame(Medellín)

#4. Analisis descriptivo de los datos 
analisis1=dataframe1.describe()
analisis2=dataframe2.describe()

#5. Mostrar resultado
print(analisis1)
print(analisis2)