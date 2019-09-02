import pandas as pd

data = pd.DataFrame(['0 /// 1', '2', '3 /// 4', '5'], columns=['yyc'])
print(data)
for index, row in data.iterrows():
    if r' /// ' in str(row['yyc']):
        print(index)
        ensembles = str(row['yyc']).split(r' /// ')
        newDf = pd.DataFrame(ensembles, columns=['yyc'])
        data = data.append(newDf, ignore_index=True)
        data.drop(index, inplace=True)
# data = data.sort_values(by=['ID'])

print(data)
# for index, row in data.iterrows():
#     print(type(index), row['yyc'])
#     if r' ///' in row['yyc']:
#         data.drop(index, inplace=True)
# print(data)