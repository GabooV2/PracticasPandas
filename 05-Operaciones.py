import numpy as np
import pandas as pd

# CONSULTAS RAPIDAS
# Rango de fechas para usar de índice en un dataframe
index = pd.date_range("2/20/2024", periods=20)

print(f"{index}\n")

# Lo utilizamos para rellenar un df con valores aleatorios
df = pd.DataFrame(np.random.randn(20, 4), index=index,
                  columns=["A", "B", "C", "D"])

print(f"{df}\n")

# Primeras 5 filas (cabeza)
print(f"{df.head()}\n")

# Primeras tres filas
print(f"{df.head(3)}\n")

# Ultimas 5 filas (cola)
print(f"{df.tail()}\n")

# Ultimas 3 filas
print(f"{df.tail(3)}\n")


# VALORES UNICOS
# Definimos un DataFrame con información de diferentes tipos
df2 = pd.DataFrame({
    'enteros': [100, 200, 300, 400],
    'decimales': [3.14, 2.72, 1.618, 3.14],
    'cadenas': ['hola', 'adiós', 'hola', 'adiós']})

print(f"{df2}\n")

# Array de valores únicos de una columna
print(f"{df2['cadenas'].unique()}\n")

# Contador de valores únicos de una columna
print(f"{df2['cadenas'].nunique()}\n")

# Dataframe con los de valores únicos y su contador de una columna
print(f"{df2['cadenas'].value_counts()}\n")

# APLICACION DE FUNCIONES
# Método interno de las Series columna
print(f"{df2['decimales'].sum()}\n")

# Aplicar una función predefinida
print(f"{df2['cadenas'].apply(len)}\n")

# Aplicar una función definida


def doblar(n):
    return n*2


print(f"{df2['enteros'].apply(doblar)}\n")

# Aplicar una función anónima
print(f"{df2['enteros'].apply(lambda n: n/3)}\n")

# Borrar permanentemente una columna
# del df2['decimales']
print(f"{df2}\n")

# RECUPERAR INDICES
# Índices de las columnas
print(f"{df2.columns}\n")

# Índice de las filas
print(f"{df2.index}\n")

# Recorrer el indice con un for
for i in df2.index:
    print(i)


# APLICAR ORDENACIONES
# Ordenar por columna (inplace=False por defecto)
print(f"{df2.sort_values(by='enteros')}\n")

# Ordenar por columna inversamente (inplace=False por defecto)
print(f"{df2.sort_values(by='enteros', ascending=False)}\n")
