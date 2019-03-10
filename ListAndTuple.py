# A1
# import copy
# l1 = eval(input())
# l2 = copy.deepcopy(l1)
# l2[0] = 0
# print(l2)
# print(l1)

# A2
# data = input().split()
# l, r = int(data[0]), int(data[1])
# lst = []
# for i in range(l, r+1):
#     lst.append(i*i)
# print(lst)

# A3
# length = int(input())
# lst = list(map(int,input().split()))
# count = 0
# for i in range(0,length):
#     for j in range(i+1, length):
#         if lst[i] + lst[j] == 9:
#             count += 1
# print(count)

# A4
# import numpy as np
# n = int(input())
# lst1, lst2 = [], []
# for i in range(0, n):
#     oneLine = list(map(int, input().split()))
#     lst1.append(oneLine)
# for i in range(0, n):
#     oneLine = list(map(int, input().split()))
#     lst2.append(oneLine)
# lst3 = np.array(lst1) + np.array(lst2)
# for oneList in lst3:
#     print(*oneList)

# A5
# import numpy as np
# n = int(input())
# lst = []
# for i in range(0, n):
#     oneLine = list(map(int, input().split()))
#     lst.append(oneLine)
# npList = np.array(lst)
# print(npList.trace())

# A6
# import numpy as np
# pList = np.array(eval(input()), dtype=float)
# qList = np.array(eval(input()), dtype=float)
# p = np.poly1d(pList)
# q = np.poly1d(qList)
# result = p*q
# regulateList = [round(i, 3) for i in result.coef]
# print(regulateList)

# A7
# s = input().split(',')
# print(type(s))
# print(','.join(sorted(s)))

# A8
# lst = list(eval(input()))
# replacement = eval(input())
# pop = int(input())
# lst[replacement[0]] = replacement[1]
# while pop in lst:
#     lst.remove(pop)
# print(lst)

# A9
# n = int(input())
# lst = list(map(int, input().split()))
# maxEle = max(lst)
# minEle = min(lst)
# for i in range(0, len(lst)):
#     if lst[i] == maxEle:
#         lst[i] = minEle
#     elif lst[i] == minEle:
#         lst[i] = maxEle
# print(*lst)

# A10
# sharedString = input()
# lst = eval(input())
# result = ['{0} {1}{2}'.format(lst.index(i), sharedString, i) for i in lst]
# print(result)

# A11
# n = int(input())
# lst = list(map(int, input().split()))
# print(*sorted(lst))

# A12
# lst = []
# try:
#     while True:
#         name = eval(input())
#         event = eval(input())
#         result = eval(input())
#         temp_tuple = (name, event, result)
#         lst.append(temp_tuple)
# except:
#     pass
# print(lst)

# A13
# lst = []
# try:
#     while True:
#         name = input()
#         event = input()
#         result = input()
#         temp_tuple = (name, event, result)
#         lst.append(temp_tuple)
# except:
#     pass
# print(lst[1][1] + ':' + lst[1][2])

# A14
# lst = []
# try:
#     while True:
#         name = eval(input())
#         event = eval(input())
#         result = eval(input())
#         temp_tuple = (name, event, result)
#         lst.append(temp_tuple)
# except:
#     pass
# outputList = []
# for oneStudent in lst:
#     if oneStudent[1] == '110M':
#         outputList.append((oneStudent[0], oneStudent[2]))
# print(outputList)
