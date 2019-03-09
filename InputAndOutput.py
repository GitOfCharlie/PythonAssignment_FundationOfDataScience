# 用来套取命令的
# try:
#     while True:
#         print(input())
# except:
#     pass

# A2
# s = input()
# n = int(input())
# f = float(input())
# print(s)
# print(n)
# print(round(f, 3))

# A3
# s = input().split()
# numbers = input().split()
# s1, s2 = s[0], s[1]
# f1, f2, f3 = float(numbers[0]), float(numbers[1]), float(numbers[2])
# print(s2, s1)
# print(round(f3, 2), round(f2, 2), round(f1, 2))
# print('{:.2f} {:.2f} {:.2f}'.format(f3, f2, f1))

# A4
# length = int(input())
# aList = [float(i) for i in input().split()]
# # aList = map(float, input().split())
# bList = [int(i)*2 for i in input().split()]
# print(*map('{:.2f}'.format, aList))
# print(*bList)
# map(函数, 迭代对象) 对每个迭代对象里的元素进行函数操作

# A5
# try:
#     while True:
#         n = int(input())
#         print(n)
# except:
#     pass

# A6
# header = input().split()
# n, m = int(header[0]), int(header[1])
# containerA, containerB = [], []
# for i in range(0, n):
#     numbers = input().split()
#     numList = map(int, numbers)
#     containerA.append(numList)
#
# try:
#     while True:
#         numbers = input().split()
#         numList = map(int, numbers)
#         containerB.append(numList)
# except:
#     pass
#
# for oneMap in containerA:
#     print(*map(lambda x: 2*x, oneMap))
# for oneMap in containerB:
#     print(sum(oneMap))

# A7
# container = []
# for i in range(0, 4):
#     content = eval(input())
#     print(content)
#     container.append(content)
# print(container)
