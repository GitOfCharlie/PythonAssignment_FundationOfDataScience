

# 1
# import numpy as np
# import random
#
# x = float(input())
# random.seed(0)
# count_0, count_1 = 0, 0
# conti_times, total_times = 0, 0
# while True:
#     total_times = total_times + 1
#     result = random.randint(2)
#     if result == 0:
#         count_0 = count_0 + 1
#     else:
#         count_1 = count_1 + 1
#     f_0 = count_0 / (count_0 + count_1)
#     f_1 = count_1 / (count_0 + count_1)
#     bias = abs(f_0-f_1)
#     # print(bias)
#     if bias < x:
#         conti_times = conti_times + 1
#     else:
#         conti_times = 0
#     if conti_times == 5:
#         break
#
# print(total_times)

# 2
# import numpy as np
# import random
# n = int(input())
# stat = {1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0}
# random.seed(0)
# for i in range(0, n):
#     a = random.randint(1, 6)
#     stat[a] = stat[a] + 1
#
# result = []
# for key in sorted(list(stat.keys())):
#     result.append('%.2f' % (stat.get(key) / n))
# print(*result)

# 3
# import random
#
# n = int(input())
# random.seed(0)
# count = 0
# for i in range(n):
#     x = random.uniform(0, 1)
#     y = random.uniform(0, 1)
#     if (x**2 + y**2) <= 1:
#         count = count + 1
#
# print('%.4f' % ((count / n)*4))

# 4
# from scipy.special import comb, perm
# n, m = tuple(map(int, input().split()))
# if n < m or m == 0:
#     print('0 0')
# else:
#     print(int(perm(n, m)), int(comb(n, m)))

# 5
# n = int(input())
# p = 1.0
# if n > 6:
#     print('0.0000')
# else:
#     for i in range(1, n+1):
#         p = p*(1 - (0.4 + 0.1 * i))
#     print('%.4f' % p)

# 6
# n, m = tuple(map(int, input().split()))
# if n == 0:
#     print('0.0000')
#     print('0.0000')
# elif n == 1 and m == 0:
#     print('1.0000')
#     print('0.0000')
# else:
#     p1 = (n / (n + m))**2
#     p2 = (n / (n + m))*((n - 1) / (n + m - 1))
#     print('%.4f' % p1)
#     print('%.4f' % p2)

# 7
# n, m = tuple(map(int, input().split()))
# p = (n / (n + m))*((m + 1) / (n + m + 1)) + (m / (n + m))*(m / (n + m + 1))
# print('%.4f' % p)

# 8
# p2, p3, p4 = tuple(map(float, input().split()))
# p1 = 1 - (p2 + p3 + p4)
# p = p1*0.5 + p2*0.15 + p3*0.1 + p4*0.05
# print('%.4f' % p)

# 9
# factory_num = int(input())
# bad_rate_list = list(map(float, input().split()))
# share_rate_list = list(map(float, input().split()))
# bad_rate = 0.0
# from_which = []
# for i in range(factory_num):
#     bad_rate = bad_rate + bad_rate_list[i]*share_rate_list[i]
# print('%.4f' % bad_rate)
# for i in range(factory_num):
#     p = share_rate_list[i]*bad_rate_list[i] / bad_rate
#     from_which.append('%.4f' % p)
# print(*from_which)

# 10
# x, a, e = tuple(map(float, input().split()))
# p1 = (a*x) / (a*x + e*(1 - x))
# p2 = ((1 - a)*x) / ((1 - a)*x + (1 - e)*(1 - x))
# print('%.6f' % p1)
# print('%.6f' % p2)

# 11
# p_list = list(map(lambda x: 1-float(x), input().split()))
# result = 1
# for i in p_list:
#     result = result*i
# print('%.4f' % (1 - result))

# 12
# def canDefeat(bin_series, damage_amount, boss_blood):
#     total_damage = 0.0
#     for j in range(len(bin_series)):
#         if bin_series[j] == '1':
#             total_damage = total_damage + damage_amount[j]
#     return total_damage >= boss_blood
#
#
# def getPossibility(bin_series, hit_rate):
#     total_possibility = 1.0
#     for k in range(len(bin_series)):
#         if bin_series[k] == '1':
#             total_possibility = total_possibility*hit_rate[k]
#         else:
#             total_possibility = total_possibility*(1-hit_rate[k])
#     return total_possibility
#
#
# n = int(input())
# hit_rate = list(map(float, input().split()))
# damage_amount = list(map(int, input().split()))
# boss_blood = int(input())
# success_rate = 0
#
# m = 2**n
# for i in range(0, m):
#     l = len(str(bin(i))[2:])
#     bin_i = '0'*(n - l) + str(bin(i))[2:]
#     if canDefeat(bin_i, damage_amount, boss_blood):
#         success_rate = success_rate + getPossibility(bin_i, hit_rate)
# print('%.4f' % success_rate)



