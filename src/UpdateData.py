import os
import pandas as pd


def downloadData(covid_19):
  if(covid_19 == 'confirmados'):
    url = 'https://cloud.minsa.gob.pe/s/Y8w3wHsEdYQSZRp/download'
    covid_19_df = pd.read_csv(url, sep=';')
  else:
    url = 'https://cloud.minsa.gob.pe/s/Md37cjXmjT9qYSa/download'
    covid_19_df = pd.read_csv(url, sep=';', encoding='latin1')

  return covid_19_df

os.makedirs('data', exist_ok=True)

covid_19  = ['fallecidos', 'confirmados']

for caso in covid_19:
  covid_19_df = downloadData(caso)
  covid_19_df.to_csv('data/'+caso+'.csv')
