import pandas as pd

# DECLARACION DE DATAFRAMES
df1 = pd.DataFrame({'A':['1A','2A'], 'B':['1B','2B'], 'C':['1C','2C']}, index=[1, 2]) 
df2 = pd.DataFrame({'A':['3A','4A','5A'], 'B':['3B','4B','5B'], 'C':['3C','4C','5C']}, index=[3, 4, 5])
df3 = pd.DataFrame({'A':['6A','7A'], 'B':['6B','7B'], 'C':['6C','7C']}, index=[6, 7])

print(f"{df1}\n")
print(f"{df2}\n")
print(f"{df3}\n")

# CONCATENACIÓN == (se utiliza para combinar columnas donde se agrega las filas al final)
df4 = pd.concat([df1, df2, df3])
print(f"{df4}\n")

# ========================================================================================

df5 = pd.DataFrame({'clave': ['K1','K2','K3'], 'A': ['1A','2A','3A'], 'B': ['1B','2B','3B']})
df6 = pd.DataFrame({'clave': ['K1','K2','K3'], 'C': ['1C','2C','3C'], 'D': ['1D','2D','3D']})

print(f"{df5}\n")
print(f"{df6}\n")

# FUSION == (se utiliza para combinar filas donde se agrega las columnas al final)
df7 = pd.merge(df5, df6, on='clave')
print(f"{df7}\n")

# ========================================================================================

df8 = pd.DataFrame({'A': ['1A','2A','3A'], 'B': ['1B','2B','3B']}, index=['K1','K2','K3'])
df9 = pd.DataFrame({'C': ['1C','2C','3C'], 'D': ['1D','2D','3D']}, index=['K1','K2','K3'])

print(f"{df8}\n")
print(f"{df9}\n")

# UNION
df10 = df8.join(df9)
print(f"{df10}\n")

