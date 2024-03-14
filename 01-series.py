import numpy as np
import pandas as pd

etiquetas = ["A", "B", "C", "D"]

lista = [25, 50, 75, 100]

# CON LISTAS
# Serie Basica
pd.Series(data=lista)

# Serie con etiquetas
pd.Series(data=lista, index=etiquetas)

# Parametros por posicion
pd.Series(lista, etiquetas)

# CON ARRAYS
array = np.random.randint(50, size=4)

# Serie Basica
pd.Series(array)

# Serie con etiquetas
pd.Series(array, etiquetas)


# INDICES
ingresos = pd.Series([100, 300, 200], index=["enero","febrero","marzo"])

print(f"{ingresos}")
print(f"{ingresos[0]}")
print(f"{ingresos['enero']}")

# METODOS

gastos = pd.Series([100, 150, 250], index=["enero","febrero","marzo"])

total = ingresos.subtract(gastos) # ó ingresos - gastos

print(f"{total}")

# SABER EL TIPO DE DATOS
type(total)
