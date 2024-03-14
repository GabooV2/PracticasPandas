import pandas as pd

# Creamos un diccionario con mucha información
ventas = {
    'Comercial': ['Juan', 'María', 'Manuel', 'Vanesa', 'Ana', 'Marcos'],
    'Empresa': ['Movistar', 'Jazztel', 'Movistar', 'Jazztel', 'Vodafone', 'Vodafone'],
    'Primas': [300, 220, 140, 70, 400, 175]
} 

df = pd.DataFrame(ventas)
# print(f"{df}\n")

# Utilizamos "groupby" para agrupar las filas en funcion del nombre de la columna (en este caso la columna "Empresa")
por_empresa = df.groupby('Empresa')

print(f"{por_empresa.mean('Primas')}\n")

print(f"{df.groupby('Empresa').mean('Primas')}\n") # directamente sin guardar el dataframe en una variable

# Desviacion Standard
print(f"{por_empresa['Primas'].std()}\n")

# Primas minimas (error)
print(f"{por_empresa.min()}\n")

# ID de la prima minima
print(f"{por_empresa['Primas'].idxmin()}\n")

# Usamos las ID de las primas minimas como fuente del df
print(f"{df.loc[por_empresa['Primas'].idxmin()]}\n")

# Usamos las ID de las primas máximas como fuente del df
print(f"{df.loc[por_empresa['Primas'].idxmax()]}\n")

# Contador de primas por empresa
print(f"{por_empresa.count()}\n")

# Reporte de analíticas descriptivas por empresa
print(f"{por_empresa.describe()}\n")

# Reporte de analíticas descriptivas por empresa
print(f"{por_empresa.describe().transpose()}\n")

# Reporte de analíticas descriptivas para una sola empresa
print(f"{por_empresa.describe().transpose()['Movistar']}\n")

