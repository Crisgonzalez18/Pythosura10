import pandas as pd

pueblos= pd.read_csv('./Siembras.csv')

#print(siembras)

#print(siembras.to_string())

#Filtro 1 quiero obtener datos del primer pueblo

Andes= pueblos[pueblos['Ciudad']=='Andes'].head(50)
print(Andes)
archivoHTML= Andes.to_html()
archivoTEXTO= open("Andes.html","w")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
