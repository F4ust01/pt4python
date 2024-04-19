import pandas as pd
from collections import Counter

def analisis_estadistico(data_frame):
    
    # Calcula la frecuencia de cada valor en la lista
    frecuencias = Counter(data_frame)
    
    # Convierte el Counter a un DataFrame de pandas
    df_frecuencias = pd.DataFrame.from_dict(frecuencias, orient='index', columns=['fi']).reset_index()
    df_frecuencias = df_frecuencias.rename(columns={'index': 'Edades'})
    
    # Ordena el DataFrame por 'Edades'
    df_frecuencias = df_frecuencias.sort_values(by='Edades').reset_index(drop=True)
    
    # Realiza la Frecuencia Absoluta Acumulada (Fi)
    df_frecuencias['Fi'] = df_frecuencias['fi'].cumsum()

    # Realiza la Frecuencia Relativa Simple (ri)
    df_frecuencias['ri'] = (df_frecuencias['fi'] / df_frecuencias['fi'].sum()).round(4)

    # Realiza la Frecuencia Relativa Acumulada (Ri)
    df_frecuencias['Ri'] = df_frecuencias['ri'].cumsum()

    # Realiza la Frecuencia Porcentual simple (pi)
    df_frecuencias['pi%'] = (df_frecuencias['ri'] * 100).round(2)

    # Realiza la Frecuencia Porcentual Acumulada (Pi)
    df_frecuencias['Pi%'] = (df_frecuencias['Ri'] * 100).round(2)

    return df_frecuencias

# Lee el archivo csv
data_frame = pd.read_csv('edades-30Alumnos.csv', skipinitialspace=True)['Edades']

print(analisis_estadistico(data_frame))