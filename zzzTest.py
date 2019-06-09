# l = [1, 2, 3]
# l2 = l + [0]*3
# print(l2)
# from collections import ChainMap
# a = ChainMap({'a': 1, 'b': 2}, {'a': 0, 'c': 3, "d": 4})
# a.parents.pop('a')
# print(a['e'])

# import re
# a = 'www'
# b = 'asjdanswwwnsasnwww'
# result = re.search(a, b)
# print(result.span())

# import numpy as np
# lst3 = np.arange(0, 0.2*5.5, 0.2)
# print(lst3)
# from scipy import stats
#
# values = [1.0, 1.0, 2.0, 1.5, 3.0]
# print(stats.binned_statistic([1, 1, 2, 5, 7], values, 'sum', bins=2))
# # help(stats.binned_statistic)

# import numpy as np
# np.random.seed(0)
# for i in range(0, 20):
#     a = np.random.randint(1, 7)
#     print(a, end=' ')

# import random
# a = random.randint(0, 1)
# print(a)

print(str(bin(7))[2:])
print(100.00 == 100.0)