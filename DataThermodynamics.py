# 1
# from sklearn import datasets
# import pandas as pd
# data_set = eval('datasets.load_'+input())()
# data = data_set.data
# print('Task 1:')
# print('\t'.join(data_set.feature_names[:3]))
# for one_record in data[:5]:
#     print('\t'.join(map(str, one_record[:3])))
#
# print()
# print('Task 2:')
# df_data = pd.DataFrame(data, columns=data_set.feature_names)
# print(df_data.head(5).iloc[:, 0:3])

# 2
# from sklearn import datasets
# import pandas as pd
# import numpy as np
#
# data_set = eval('datasets.load_'+input())()
# data_target = pd.Series(data_set.target)
# value_stat = dict(data_target.value_counts())
# # print(value_stat)
# p_stat = {}
# for key, value in value_stat.items():
#     p = value / sum(value_stat.values())
#     p_stat[key] = p
# H = 0
# for key, p in p_stat.items():
#     H += -(p*np.log(p))
# print('%.4f' % H)

# 3
from sklearn import datasets
import pandas as pd
import numpy as np
import sys
import datetime


def get_entropy(target):
    data_target = pd.Series(target)
    value_stat = dict(data_target.value_counts())
    p_stat = {}
    for key, value in value_stat.items():
        p = value / sum(value_stat.values())
        p_stat[key] = p
    H = 0
    for key, p in p_stat.items():
        H += -(p*np.log(p))
    return H


def get_conditionEntropy(df: pd.DataFrame):
    H = 0
    # class_list = dict(df['class'].value_counts()).keys()
    # target_list = dict(df['target'].value_counts()).keys()

    # for x in class_list:
    #     p_x = df[df['class'] == x].shape[0] / df.shape[0]
    #     for y in target_list:
    #         p_xy = df[(df['class'] == x) & (df['target'] == y)].shape[0] / df.shape[0]
    #         p_yfromx = p_xy / p_x
    #         if not p_yfromx == 0:
    #             H += -(p_xy*np.log(p_yfromx))
    lst = []
    for i in [0, 1, 2]:
        divideDf1 = df[(df['target'] == i) & (df['class'] == 0)]
        divideDf2 = df[(df['target'] == i) & (df['class'] == 1)]
        lst.append(divideDf1.shape[0])
        lst.append(divideDf2.shape[0])
    # print(lst)
    for x in [0, 1]:
        p_x = (lst[0+x] + lst[2+x] + lst[4+x]) / sum(lst)
        if p_x == 0:
            continue
        for y in [0, 1, 2]:
            p_xy = lst[2*y+x] / sum(lst)
            p_yfromx = p_xy / p_x
            if not p_yfromx == 0:
                H += -(p_xy*np.log(p_yfromx))
    return H


if __name__ == '__main__':
    data_set = datasets.load_wine()
    df = pd.DataFrame(data=data_set['data'], columns=data_set['feature_names'])
    df['target'] = data_set.target
    print(df['alcohol'])
    print(df['alcohol'].shape[0], df.shape[0])
    quit()
    origin_entropy = get_entropy(data_set.target)

    feature_name = input()
    min_conditionEntropy, min_xValue = sys.maxsize, df[feature_name].min()
    for x in df[feature_name].unique():
        class_list = [0 if i <= x else 1 for i in df[feature_name]]
        df['class'] = class_list
        conditionEntropy = get_conditionEntropy(df)
        if conditionEntropy < min_conditionEntropy:
            min_conditionEntropy = conditionEntropy
            min_xValue = x

    print('%.6f' % origin_entropy, '%.6f' % min_conditionEntropy)
    print(min_xValue)

# 4
# from sklearn import datasets
# import pandas as pd
# import numpy as np
#
#
# def get_relativeEntropy(target_p: pd.Series, target_q: pd.Series):
#     p_stat = get_targetStatistics(target_p)
#     q_stat = get_targetStatistics(target_q)
#     KL = 0
#     for x in p_stat.keys():
#         px, qx = p_stat[x], q_stat[x]
#         KL += px*np.log(px/qx)
#     return KL
#
#
# def get_targetStatistics(target: pd.Series):
#     value_stat = dict(target.value_counts())
#     p_stat = {}
#     for key, value in value_stat.items():
#         p = value / sum(value_stat.values())
#         p_stat[key] = p
#     return p_stat
#
#
# if __name__ == '__main__':
#     set_name = input()
#     data_set = eval('datasets.load_{}()'.format(set_name))
#     if set_name == 'digits':
#         df = pd.DataFrame(data=data_set['data'])
#     else:
#         df = pd.DataFrame(data=data_set['data'], columns=data_set['feature_names'])
#     df['target'] = data_set['target']
#     for X in [0.01, 0.1, 0.5, 0.9]:
#         sample_df = df.sample(frac=X, random_state=0)
#         print('%.6f' % get_relativeEntropy(sample_df['target'], df['target']))

# 5
# from sklearn import datasets
# import pandas as pd
#
#
# def stratifiedSample(df: pd.DataFrame) -> pd.DataFrame:
#     # value_counts, groupby
#     # sample(n=, random_state=0)
#     new_df = pd.DataFrame(data=None, columns=df.columns)
#     # min_num = dict(df['target'].value_counts())
#     min_num = df['target'].value_counts().min()
#
#     targets = list(df.drop_duplicates(['target'])['target'])
#     for target in targets:
#         one_sample = df[df.target == target].sample(n=min_num, random_state=0)
#         new_df = new_df.append(one_sample)
#         # new_df = pd.concat([new_df, one_sample])
#     return new_df  # TODO
#
#
# dataset = eval('datasets.load_{}()'.format(input()))
#
# feature_names = dataset['feature_names']
#
# df = pd.DataFrame(data=dataset['data'],
#                   columns=feature_names)
# df['target'] = dataset['target']
#
# print(stratifiedSample(df)[feature_names[:3]].describe())

