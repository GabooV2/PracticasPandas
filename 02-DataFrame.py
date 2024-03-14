import numpy as np
import pandas as pd

array = np.random.uniform(-10, 10, size=[4, 4])

df = pd.DataFrame(array, index=["A", "B", "C", "D"], columns=["W", "X", "Y", "Z"])

print(df)

type(df) # para saber el tipo de datos que son los data frame

print(f"\n{df['X']}")
print(f"\n{df[['Y', 'Z']]}")

# AÑADIR UNA NUEVA COLUMNA

df['TOTAL'] = df["W"] + df['X'] + df['Y'] + df['Z']
print(f"\n{df}")

# BORRAR COLUMNA
df.drop('TOTAL', axis=1, inplace=True) # PARA BORRAR UNA COLUMNA EL "AXIS" ES IGUAL A 1 --  PARA FILAS EL "AXIS" ES IGUAL A 0
print(f"\n{df}")                       # "inplace=True" INDICA QUE EFECTIVAMENTE SE BORRA DEL DATA FRAME

# SELECCIONAR O CONSULTAR UNA FILA
print(f"\n{df.loc['C']}") # POR LA ETIQUETA
print(f"\n{df.iloc[2]}") # POR EL INDICE DE LA ETIQUETA

# SELECCIONAR SUBSET
print(f"\n El elemento que esta en la interseccion de C con Z es: {df.loc['C','Z']}")

print(f"\n{df.loc[['A','B'],['W','Y']]}")

# SELECCION CONDICIONADA
print(f"\n{df>0}") # DEVUELVE TRUE O FALSE
print(f"\n{df[df>0]}") # DEVUELVE LOS VALORES QUE CMPLEN CON LA CONDICION Y EL RESTO SE DEVUELVE COMO "NaN"

print(f"\n{df[df['X']>0]}") # DEVUELVE EL VALOR SOLO DE LAS FILAS EN DONDE X ES > 0

print(f"\n{df[df['X']>0][['Y','Z']]}") # DEVUELVE EL VALOR DE LAS COLUMNAS Y y Z SOLO DE LAS FILAS EN DONDE X ES > 0

print(f"\n{df[(df['X']>0) | (df['X']<0)]}") # EL SIMBOLO "|" SIGNIFICA EL OPERADOR "OR" Y EL SIMBOLO "&" SIGNIFICA EL OPERADOR "AND"

print(f"\n{df[(df['X']>0) | (df['X']<0)][['Y','Z']]}") # COMBINANDO UN POCO LO APRENDIDO

print(f"\n{df[(df['X']>0) | (df['X']<0)]['Y']}") # COMBINANDO UN POCO LO APRENDIDO


# MOODIFICANDO LOS INDICES
df['CODIGOS'] = ["AA", "BB", "CC", "DD"]
print(f"\n{df}")

df.set_index('CODIGOS', inplace=True) # SE CONFIGURA PARA QUE LA SERIE "CODIGOS" SEA LA NUEVA COLUMNA DE INDICE DEL DATA FRAME
print(f"\n{df}")

print(f"\n{df.loc['AA']}")
print(f"\n{df.loc[['AA','CC']]}")


# INDICES POR DEFECTO
df.reset_index(drop=True, inplace=True) # RESETEA EL VALOR DE LOS INDICES POR DEFECTO
print(f"\n{df}")


