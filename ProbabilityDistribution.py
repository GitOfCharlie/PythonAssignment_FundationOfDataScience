# 1
# r = int(input())
#
# if r <= 1:
#     p = 1
# else:
#     p = 1 / r**2
#
# e = r*2/3
# var = r**2 / 18
# print('%.4f' % p)
# print('%.4f' % e)
# print('%.4f' % var)

# 2
# data = input().split()
# n, p = int(data[0]), float(data[1])
# x_list = list(range(0, n + 1))
# p_list = []
# for x in x_list:
#     if x == n:
#         p_x = (1 - p)**x
#     else:
#         p_x = ((1 - p)**x)*p
#     p_list.append(p_x)
# # EX = sum(np.array(x_list, dtype=np.int)*np.array(p_list, dtype=np.float))
# EX = sum([a * b for a, b in zip(x_list, p_list)])
# EX2 = sum([(a**2) * b for a, b in zip(x_list, p_list)])
# VarX = EX2 - EX**2
# print('X\t' + '\t'.join(map(str, x_list)))
# print('P\t' + '\t'.join(map(lambda p: '%.4f' % p, p_list)))
# print('%.4f' % EX)
# print('%.4f' % VarX)

# 3
# import math
# from scipy.special import comb, perm
# n = int(input())
# a = 0
# p = 0.0
# while p <= 0.99:
#     p = p + comb(n, a) * math.pow(0.01, a) * math.pow(0.99, n - a)
#     a = a + 1
# print(a-1)

# 4
# from scipy.special import comb, perm
# n = int(input())
# slits = []
# for i in range(n+1):
#     val = (0.5**n)*comb(n, i)
#     slits.append('%.4f' % val)
# print(*slits)

# 5
# from scipy.stats import binom, poisson
# p, n = tuple(map(eval, input().split()))
# p_binom = binom(n, p).cdf(2)
# print('%.6f' % p_binom)
# p_poisson = poisson(n*p).cdf(2)
# print('%.6f' % p_poisson)

# 6
# p = float(input())
# print('%.4f' % (1/p))
# print('%.4f' % ((1 - p) / p**2))

# 7
# n = int(input())
# print('%.6f' % (3*0.02*0.98*0.98))
# p1 = 0.02*(0.98*n/(n-1))*((0.98*n-1)/(n-2))
# p2 = 0.98*(0.02*n/(n-1))*((0.98*n-1)/(n-2))
# p3 = 0.98*((0.98*n-1)/(n-1))*((0.02*n)/(n-2))
# print('%.6f' % (p1+p2+p3))

# 8
# import math
# n = int(input())
# r = 0.001
# p = math.exp(-r*n)
# print('%.6f' % p)

# 9
# import scipy.stats as st
# c, p = tuple(map(eval, input().split()))
# z = st.norm.ppf(1 - p)
# d = c - 0.5*z
# print('%.2f' % d)

# 10
# import scipy.stats as st
# p1, p2 = tuple(map(eval, input().split()))
# z1 = st.norm.ppf(p1)
# z2 = st.norm.ppf(1 - p2)
# cita = 50 / (z2 - z1)
# miu = 500 - (50*z1) / (z2 - z1)
# print('%.4f' % miu, '%.4f' % cita)





