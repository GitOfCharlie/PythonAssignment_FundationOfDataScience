# A1
# year = int(input())
# if year % 4 == 0 and year % 100 != 0:
#     print(True)
# elif year % 400 == 0:
#     print(True)
# else:
#     print(False)

# A2
# lst = list(map(int, input().split()))
# lst.sort()
# print(*lst)

# A3
# import math
# profit = int(input())
# bonus = 0
# if profit <= 100000:
#     bonus = profit*0.1
# elif 100000 < profit < 200000:
#     bonus = 100000*0.1 + (profit - 100000)*0.075
# elif 200000 <= profit <= 400000:
#     bonus = 100000*0.1 + 100000*0.075 + (profit - 200000)*0.05
# elif 400000 <= profit <= 600000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000*0.05 + (profit - 400000)*0.03
# elif 600000 <= profit <= 1000000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000*0.05 + 200000*0.03 + (profit - 600000)*0.015
# elif profit > 1000000:
#     bonus = 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000*0.015 + (profit - 1000000)*0.01
# print(math.floor(bonus))

# A4
# def isDaffodil(x):
#     if x < 100 or x > 1000:
#         return False
#     else:
#         a = x % 100
#         b = (x / 10) % 10
#         c = x % 10
#         result = a**3 + b**3 + c**3
#         return result == x
#
#
# if __name__ == '__main__':
#     number = int(input())
#     temp1, temp2 = number, number
#     while not isDaffodil(temp1):
#         temp1 -= 1
#     while not isDaffodil(temp2):
#         temp2 += 1
#     if temp2 > 1000 or number - temp1 <= temp2 - number:
#         print(temp1)
#     else:
#         print(temp2)

# A5
# num = int(input())
# count = 1
# while (int('9'*count) % num != 0):
#     count += 1
# print(count)

# A6
# data = input().split()
# weight, height = int(data[0]), int(data[1])/100
# BMI = weight/(height**2)
# print('Your BMI is {:.1f}, '.format(BMI), end='')
# if BMI < 18.5:
#     print('too thin')
# elif 18.5 <= BMI < 24:
#     print('normal')
# elif 24 <= BMI < 28:
#     print('overweight')
# else:
#     print('fat')

# A7
# x = 7
# while x % 3 != 2 or x % 5 != 4 or x % 6 != 5:
#     x += 14
# print(x)

# A8
# lst = eval(input())
# grade = []
# for i in lst:
#     if i >= 90:
#         grade.append('A')
#     elif i >= 80:
#         grade.append('B')
#     elif i >= 70:
#         grade.append('C')
#     elif i >= 60:
#         grade.append('D')
#     else:
#         grade.append('F')
# print(grade)

# A9
