import numpy as np
import math
import pandas as pd

data = pd.read_excel('F:\\Desktop\\IDandEnsembl.xlsx')

appendDf = pd.DataFrame(columns=['ID', 'Ensembl'])

for index, row in data.iterrows():
    if r' /// ' in str(row['Ensembl']):
        ensembles = str(row['Ensembl']).split(r' /// ')
        newDf = pd.DataFrame(ensembles, columns=['Ensembl'])
        newDf['ID'] = str(row['ID'])
        appendDf = appendDf.append(newDf, ignore_index=True)
        data.drop(index, inplace=True)

data = data.append(appendDf)
data = data.sort_values(by=['ID'])
# print(data.head(12))
data.to_csv('F:\\Desktop\\wtf.csv')
