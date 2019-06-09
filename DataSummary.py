# import numpy as np

# 1
# import numpy as np
# size = int(input())
# lst1 = np.array(input().split(), dtype=np.int64)
# lst2 = np.zeros([size])
# lst3 = np.arange(0, 0.2*(size-0.5), 0.2)
# lst4 = np.linspace(0, 2, size)
# np.random.seed(size)
# lst5 = np.random.uniform(1, 3, size)
# lst0 = (lst1+lst2+lst3+lst4+lst5).reshape((2, int(size/2)))
# print('ndim: '+str(lst0.ndim)+', shape: '+str(lst0.shape)+', size: '+str(lst0.size)+', itemsize: '+str(lst0.itemsize)+', dtype: '+str(lst0.dtype))
# print(lst0)

# 2
# import numpy as np
# size = int(input())
# a1 = np.array(input().split(), dtype=np.int64)
# np.random.seed(size)
# a2 = np.random.randint(0, 10, size)
# a1 = a1.reshape((2, int(size/2)))
# a2 = a2.reshape((2, int(size/2)))
# print('sum: '+str(a1.sum())+', min: '+str(a1.min())+', max: '+str(a1.max()))
# print('a1 + a2:')
# print(' ', end='')
# print(a1+a2)
# print('a1 * a2:')
# print(' ', end='')
# print(a1*a2)
# print('a1 ** a2:')
# print(' ', end='')
# print(a1**a2)
# print('a2.T x a1:')
# print(' ', end='')
# print(a2.T.dot(a1))

# 3
# import numpy as np
# seed = int(input())
# np.random.seed(seed)
# a = np.random.randint(0, 20, (3, 4), dtype=np.int64)
# print('a:\n', a)
# ha1, ha2 = np.hsplit(a, indices_or_sections=2)
# print('ha1:\n', ha1)
# va1, va2, va3 = np.vsplit(a, indices_or_sections=3)
# print('va1:\n', va1)
# h_stack = np.hstack((ha1, ha2))
# print('hstack:\n', h_stack)
# v_stack = np.vstack((va1, va2))
# print('vstack:\n', v_stack)
# print('a:\n', a.flatten(order='C'))

# 4
import numpy as np
import pandas as pd

lst = np.array(input().split(), dtype=np.float)
bins = list(range(0, int(np.ceil(np.max(lst)))+3, 3))
new_lst = pd.cut(lst, bins, right=False)
counts = dict(pd.value_counts(new_lst))
max_value = max(counts.values())
for one_section in sorted(list(counts.keys())):
    if counts.get(one_section) == max_value:
        print(one_section)

# 5
# def getMedian(q, lst):
#     if q+0.5 == int(q+0.5):
#         median = (lst[int(q-0.5)-1] + lst[int(q+0.5)-1])/2
#     else:
#         median = lst[round(q)-1]
#     return median
#
#
# import numpy as np
# lst = np.array(input().split(), dtype=np.float)
# lst.sort()
# n = len(lst)
# result1, result2 = [], []
# for i in [1, 2, 3]:
#     q1 = 1+i*(n-1)/4
#     q2 = i*(n+1)/4
#     median1 = getMedian(q1, lst)
#     result1.append('%.2f' % median1)
#     median2 = getMedian(q2, lst)
#     result2.append('%.2f' % median2)
# print(*result1)
# print(*result2)

# 6
# import numpy as np
# from scipy import stats
# lst = np.array(input().split(), dtype=np.float)
# A = np.mean(lst)
# G = stats.gmean(lst)
# H = stats.hmean(lst)
# new_lst = np.array(list(map(lambda x: x**2, lst)))
# Q = np.sqrt((np.sum(new_lst)) / len(new_lst))
# result = list(map(lambda x: '%.4f' % x, [A, G, H, Q]))
# print(*result)

# 7
# def getMedian(q, lst):
#     if q+0.5 == int(q+0.5):
#         median = (lst[int(q-0.5)-1] + lst[int(q+0.5)-1])/2
#     else:
#         median = lst[round(q)-1]
#     return median
#
# import numpy as np
# lst = np.array(input().split(), dtype=np.float)
# lst.sort()
# n = len(lst)
# result = []
# for i in [1, 2, 3]:
#     q = 1+i*(n-1)/4
#     median = getMedian(q, lst)
#     result.append(median)
# print('%.2f' % (np.max(lst)-np.min(lst)), '%.2f' % (result[2]-result[0]))

# 8
# import numpy as np
# lst = np.array(input().split(), dtype=np.float)
# print('%.2f' % (np.var(lst)*len(lst)), '%.2f' % np.var(lst), '%.2f' % np.std(lst))