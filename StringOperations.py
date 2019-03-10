# A1
# n = input()
# print(int(n*2018)%84)

# A2
# s = input()
# print(s[::-1])

# A3
# s = input()
# print(s == s[::-1])

# A4
# s = input()
# print(s[:3], s[3:6], s[6:])

# A5
# s = list(input())
# print(len(s))
# print(*s)

# A6
# for i in range(1, 8):
#     numOfSpace = abs(4 - i)
#     print(' '*numOfSpace, end='')
#     if i <= 4:
#         print('*'*(2*i-1))
#     else:
#         print('*'*(2*(8 - i)-1))

# A7
# date = list(input().split())
# if int(date[1]) < 10:
#     date[1] = '0' + date[1]
# if int(date[2]) < 10:
#     date[2] = '0' + date[2]
# print('-'.join(date))

# A8
# a = int(input())
# b = bin(a)[2:]
#

# A9
# s = input()
# print(s.swapcase())

# A10
# s = input()
# if s[0:1].isupper() and s[1:].islower():
#     print(True)
# else:
#     s = s[0:1].upper() + s[1:].lower()
#     print(s)

# A11
# info = input()
# info = info[0:1].upper() + info[1:].lower()
# lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for day in lst:
#     if day.startswith(info):
#         print(day)
#         break

# A12
# info = list(input())
# alphaList = [s for s in info if s.isalpha()]
# print(''.join(alphaList))

# A13
# s1, s2 = input(), input()
# l1, l2 = len(s1), len(s2)
# count = 0
# for i in range(0, l1-l2+1):
#     if s1[i:i+l2] == s2:
#         count += 1
# print(count)

# A14
# originS = list(input())
# for i in range(0, len(originS)):
#     if originS[i].isalpha():
#         if originS[i] in ['A', 'B', 'C', 'D', 'E']:
#             originS[i] = chr(ord(originS[i]) + 21)
#         else:
#             originS[i] = chr(ord(originS[i])-5)
# print(''.join(originS))
