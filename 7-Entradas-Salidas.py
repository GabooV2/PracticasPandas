import numpy as np
import pandas as pd

# # Definimos un dataframe con datos de ejemplos
# df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])

# # GUARDAR EN FORMATO .CSV
# df.to_csv('datos.csv', index=False)
# del(df)

# # CARGAR UN ARCHIVO .CSV
# df = pd.read_csv('datos.csv')
# print(f"{df}\n")

# # GUARDAR EN FORMATO .JSON
# df.to_json('datos.json')

# # GUARDAR EN FORMATO .XLSX
# df.to_excel('datos.xlsx', sheet_name='Sheet1', index=False)
# del(df)

# # CARGAR UN ARCHIVO .XLSX
# df = pd.read_excel('datos.xlsx', sheet_name='Sheet1')
# print(f"{df}\n")

# GUARDAR INFORMACION HTML
df = pd.read_html('https://web.archive.org/web/20220717170349/https://en.wikipedia.org/wiki/List_of_countries_by_past_fertility_rate')

#Como la pagina nos trae varias tablas guardamos la tabla que queremos (en este caso nos guardamos la tabla 3 en la posicion 2)
fertility_rate = df[2]
# print(f"{fertility_rate.head()}\n")   # mostramos los primero 5 registros

# Renombramos la primera columna para que sea más fácil consultarla
fertility_rate.rename(columns = {'Country/dependent territory':'Country'}, inplace=True)
# print(f"{fertility_rate}\n")

# Índice de natalidad por país entre los años 2010-2015
# print(f"{fertility_rate[['Country', '20102015']]}\n")

# Misma consulta aplicando el styler para esconder la primera columna
# print(fertility_rate[['Country', '2010–2015']].head().to_string(index=False)) # el style.hide (PARA JUPYTER) se cambio por to_string ya que daba error

# # Índice de natalidad por país entre los años 1985–1990 ordenado de más a menos (primeros resultados)
# print(fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).head().to_string(index=False))

# # Índice de natalidad por país entre los años 1985–1990 ordenado de más o menos (últimos resultados)
# print(fertility_rate[["Country", "1985–1990"]].sort_values(by="1985–1990", ascending=False).tail().to_string(index=False))

# # Vamos a transformar todas las columnas desde la segunda hasta la última a valores númericos
fertility_rate = fertility_rate[1:][:].apply(pd.to_numeric, errors='coerce')

# # Ahora podemos consultar la media del índice de natalidad para cada año
# print(fertility_rate.mean()[1:])

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = 10,5

fertility_rate.mean()[1:].plot(kind='line', xlabel="Períodos", ylabel="Media de natalidad mundial")
plt.show()