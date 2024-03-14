import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [7, 8, -6, 8],
    'B': [12, np.nan, 1, np.nan],
    'C': [4, np.nan, np.nan, np.nan],
    'D': [4, np.nan, -2, -10]
})

print(f"{df}\n")

# Comprobar registros nulos
print(f"{df.isnull()}\n")

# Descartar filas con registros nulos
print(f"{df.dropna()}\n")

# Descartar columnas con registros nulos
print(f"{df.dropna(axis=1)}\n")

# Mostrar filas con un minimo de registros no nulos (en este caso 2 registros)
print(f"{df.dropna(thresh=2)}\n")

# Rellenar los registros nulos por un valor por defecto
print(f"{df.fillna(value=0)}\n")

# Rellenar los registros de las filas vacias de la columna con el valor minimo de esa misma columna (en este caso la columna B)
print(f"{df['B'].fillna(value=df['B'].min())}\n")

# Rellenar los registros de las filas vacias de la columna con el valor maximo de esa misma columna (en este caso la columna B)
print(f"{df['B'].fillna(value=df['B'].max())}\n")


