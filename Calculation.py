# A1
# head = input().split()
# x, y = int(head[0]), int(head[1])
# print('{0} + {1} = {2}'.format(x, y, x + y))
# print('{0} - {1} = {2}'.format(x, y, x - y))
# print('{0} * {1} = {2}'.format(x, y, x*y))
# print('{0} // {1} = {2}'.format(x, y, x // y))

# A2
# lst = list(map(int, input().split()))
# a = int((lst[0] + lst[2])/2)
# b = a - lst[0]
# c = b - lst[1]
# if b + c != lst[3] or a < 0 or b < 0 or c < 0:
#     print('None')
# else:
#     print(a, b, c)

# A3
# x = float(input())
# y = 2*(x**2) + 3*x - 5
# print('{:.1f}'.format(y))

# A4
# F = float(input())
# C = (5/9)*(F-32)
# print('{:.2f}'.format(C))

# A5
# head = input().split()
# x, y = int(head[0]), int(head[1])
# print(x & y)
# print(x | y)
# print(x ^ y)
# x1, y1 = ~x, ~y
# print(min(x1, y1))

# A6
# x = int(input())
# bin_x = bin(x)[-4:]
# print(int(bin_x, 2))

# A7
# data = list(map(int, input().split()))
# print(data[0]*data[1]*data[2])

# A8
# import math
# data = list(map(float, input().split()))
# a, b, c = data[0], data[1], data[2]
# if a+b > c and a+c > b and b+c > a:
#     p = (a + b + c)/2
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print('{:.3f}'.format(s))
# else:
#     print(0)

# A9
# lst = []
# for i in range(100, 1000):
#     num = str(i)
#     result = int(num[0])**3 + int(num[1])**3 + int(num[2])**3
#     if result == i:
#        lst.append(i)
# print(*lst)
