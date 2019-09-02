

# 1
# n, m = tuple(map(int, input().split()))
# p00 = (m / (n+m))*((m-1) / (n+m-1))
# p01 = (m / (n+m))*(n / (n+m-1))
# p10 = (n / (n+m))*(m / (n+m-1))
# p11 = (n / (n+m))*((n-1) / (n+m-1))
# print('X\Y\t0\t1')
# print('0\t'+'%.4f' % p00+'\t'+'%.4f' % p01)
# print('1\t'+'%.4f' % p10+'\t'+'%.4f' % p11)

# 2
# a, b, c = tuple(map(float, input().split()))
# p_0 = a + c
# p1_ = a / p_0
# p12 = p1_ - a - b
# p_1 = b / p1_
# p_2 = p12 / p1_
# p21 = p_1 - b
# p22 = p_2 - p12
# p2_ = c + p21 + p22
# print('P(i,j)\tj=0\tj=1\tj=2\tP(i)')
# print('i=1\t'+'\t'.join(['%.4f' % a, '%.4f' % b, '%.4f' % p12, '%.4f' % p1_]))
# print('i=2\t'+'\t'.join(['%.4f' % c, '%.4f' % p21, '%.4f' % p22, '%.4f' % p2_]))
# print('P(j)\t'+'\t'.join(['%.4f' % p_0, '%.4f' % p_1, '%.4f' % p_2, '%.4f' % 1]))

# 3
# from scipy.integrate import quad, dblquad, tplquad
# a, b = tuple(map(float, input().split()))
# if a >= 1:
#     p1 = 0
# else:
#     B = min(1.0, b)
#     val, err = dblquad(lambda y, x: (2/(b**2-a**2)), a, B, lambda x: x**2, lambda x: x)
#     p1 = val
#
# p2 = (0.3**2 - a**2) / (b**2 - a**2)
# p2 = max(0.0, p2)
# p2 = min(1.0, p2)
#
# print('%.4f' % p1)
# print('%.4f' % p2)

# 4
# def A(k: int, x):
#     x = [i**k for i in x]
#     u = sum(x) / len(x)
#     return u# TODO return Ak
#
#
# def B(k: int, x):
#     if k == 1:
#         return 0.0000
#     average_x = sum(x) / len(x)
#     x = [(i-average_x)**k for i in x]
#     v = sum(x) / len(x)
#     return v# TODO return Bk
#
# import math
# x = list(map(float, input().split()))
# for k in range(1, 5):
#     print('{:.4f} {:.4f}'.format(A(k, x), B(k, x)))

# 5
# def A(k: int, x):
#     x = [i**k for i in x]
#     u = sum(x) / len(x)
#     return u# TODO return Ak
#
#
# def B(k: int, x):
#     if k == 1:
#         return 0.0000
#     average_x = sum(x) / len(x)
#     x = [(i-average_x)**k for i in x]
#     v = sum(x) / len(x)
#     return v# TODO return Bk
#
# import math
# salary = list(map(float, input().split()))
# skewness = B(3, salary) / math.pow(B(2, salary), 1.5)
# kurtosis = B(4, salary) / math.pow(B(2, salary), 2)
# print('%.4f' % skewness, '%.4f' % kurtosis)

# 6
# def mixedMoment(data, k: int, l: int):
#     result = [(i[0]**k)*(i[1]**l) for i in data]
#     return sum(result) / len(result) # TODO
#
#
# def mixedCentralMoment(data, k: int, l: int):
#     x_ = sum([i[0] for i in data]) / len(data)
#     y_ = sum([i[1] for i in data]) / len(data)
#     result = [((i[0]-x_) ** k) * ((i[1]-y_) ** l) for i in data]
#     return sum(result) / len(result) # TODO
#
#
# x = map(float, input().split())
# y = map(float, input().split())
#
# points = list(zip(x, y))
#
# while True:
#     try:
#         k, l = map(int, input().split())
#         print('{:.4f} {:.4f}'.format(
#             mixedMoment(points, k, l),
#             mixedCentralMoment(points, k, l)))
#     except EOFError:
#         break

# 7
# import numpy as np
# list1 = np.array(list(map(float, input().split())))
# list2 = np.array(list(map(float, input().split())))
# covxy = np.mean((list1-list1.mean()) * (list2-list2.mean()))
# std1 = np.std(list1)
# std2 = np.std(list2)
# coefxy = covxy / (std1*std2)
# print('%.4f' % covxy, '%.4f' % coefxy)

# 8
# import math
# def pnorm(X, p):
#     if p == 'inf':
#         Y = max([math.fabs(i) for i in X])
#     else:
#         Y = math.pow(sum([math.fabs(i)**p for i in X]), 1/p)
#     return Y # TODO
#
#
# X = list(map(float, input().split()))
#
# p = input()
# p = int(p) if p != 'inf' else p
#
# print('{:.4f}'.format(pnorm(X, p)))

# 9
# import math
#
#
# def getDistance(X, Y, p):
#     if p == 'inf':
#         return max([abs(i-j) for i, j in zip(X, Y)])
#     return math.pow(sum([math.fabs(i-j)**p for i, j in zip(X, Y)]), 1/p)
#
#
# X = tuple(map(float, input().split()))
# Y = tuple(map(float, input().split()))
# print('%.4f' % getDistance(X, Y, 1), '%.4f' % getDistance(X, Y, 2), '%.4f' % getDistance(X, Y, 'inf'))

# 10
# import numpy as np
# import math
# X = np.array(list(map(float, input().split())))
# Y = np.array(list(map(float, input().split())))
# t = sum(X*Y)
# s = sum(X**2)
# similarity = sum(X*Y) / (math.sqrt(sum(X**2)) * math.sqrt(sum(Y**2)))
# print('%.4f' % similarity)

