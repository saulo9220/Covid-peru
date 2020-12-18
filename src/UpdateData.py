import os
import pandas as pd

def downloadData(covid_19):
  if(covid_19 == 'confirmados'):
    url = 'https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download'
    campo_fecha = 'FECHA_RESULTADO'
    covid_19_df = pd.read_csv(url, sep=';')
  else:
    url = 'https://cloud.minsa.gob.pe/s/Md37cjXmjT9qYSa/download'
    campo_fecha = 'FECHA_FALLECIMIENTO'
    covid_19_df = pd.read_csv(url, sep=';', encoding='latin1')

  return covid_19_df, campo_fecha

os.makedirs('data', exist_ok=True)
os.makedirs('dataset', exist_ok=True)

covid_19  = ['fallecidos', 'confirmados']

for caso in covid_19:
  covid_19_df, campo_fecha = downloadData(caso)
  covid_19_df.to_csv('data/'+caso+'.csv')

  dataset_df = covid_19_df[['DEPARTAMENTO', campo_fecha]]
  registros_vacios = dataset_df[campo_fecha].isnull().sum()
  
  if(registros_vacios > 0):
     dataset_df = dataset_df.dropna()

  df = dataset_df

  df['CONFIRMADOS'] = [1 for i in range(len(df))]

  def __formatear_fecha(df_fecha):
    lista = []
    for fecha in df_fecha: 
      fecha = str(fecha)
      fecha = fecha[0:4]+'-'+fecha[4:6]+'-'+fecha[6:8]
      lista.append(fecha)
    return lista

  df['FECHA'] = __formatear_fecha(df[campo_fecha])
  df = df.drop([campo_fecha], axis=1)
  df = df.pivot_table(index='FECHA', columns='DEPARTAMENTO', values='CONFIRMADOS', aggfunc='sum')
  df.fillna(0, inplace=True)

  peru_df = pd.DataFrame()
  peru_df['PERÚ'] = df['AMAZONAS']*0

  for i in df.columns:
    peru_df['PERÚ'] = peru_df['PERÚ']+df[i] 
  df['PERÚ'] = peru_df.values.astype('float')

  df.to_csv('dataset/'+caso+'.csv')

