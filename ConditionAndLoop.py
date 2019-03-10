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
#         a = x / 100
#         b = (x / 10) % 10
#         c = x % 10
#         result = a**3 + b**3 + c**3
#         return result == x
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
# __________________________________________________________
# number = int(input())
# high = 1000
# low = 100
# for i in range(number, 1000):
#     num = str(i)
#     a = int(num[0])
#     b = int(num[1])
#     c = int(num[2])
#     if a**3 + b**3 + c**3 == i:
#         high = i
#         break
# for i in range(number, 100, -1):
#     num = str(i)
#     a = int(num[0])
#     b = int(num[1])
#     c = int(num[2])
#     if a**3 + b**3 + c**3 == i:
#         low = i
#         break
# if high == 1000:
#     print(low)
# elif low == 100:
#     print(high)
# elif high - number < number - low:
#     print(high)
# else:
#     print(low)


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
# n = int(input())
# for i in range(1, n+1):
#     expressions = []
#     for j in range(1, i+1):
#         oneExpression = '{0}*{1}={2}'.format(i, j, i*j)
#         expressions.append(oneExpression)
#     print(' '.join(expressions))

# A10
# daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# data = input().split('-')
# year, month, day = int(data[0]), int(data[1]), int(data[2])
# if year % 4 == 0 and year % 100 != 0:
#     daysOfMonth[2] += 1
# elif year % 400 == 0:
#     daysOfMonth[2] += 1
# sum = 0
# for i in range(1, month):
#     sum += daysOfMonth[i]
# sum += day
# print(sum)

# A11
# salary = int(input())
# if salary <= 3500:
#     rate = 0
#     bias = 0
# elif 3500 < salary <= 5000:
#     rate = 0.03
#     bias = 0
# elif 5000 < salary <= 8000:
#     rate = 0.1
#     bias = 105
# elif 8000 < salary <= 12500:
#     rate = 0.2
#     bias = 555
# elif 12500 < salary <= 38500:
#     rate = 0.25
#     bias = 1005   
# elif 38500 < salary <= 58500:
#     rate = 0.3
#     bias = 2755
# elif 58500 < salary <= 83500:
#     rate = 0.35
#     bias = 5505
# elif salary > 83500:
#     rate = 0.45
#     bias = 13505
# tax = (salary - 3500)*rate - bias
# print(round(tax))

# A12
# n = int(input())
# count = 0
# for i in range(1, n+1):
#     temp = list(str(i))
#     bits = [int(i) for i in temp]
#     if sum(bits)%5 == 0:
#         count += 1
# print(count)

# A13
# import math
# num = list(input())
# isValid = True
# for i in num:
#     if i in ['8', '9']:
#         isValid = False
#         break
# if not isValid:
#     print('Invalid octal number!')
# else:
#     num.reverse()
#     sum = 0
#     for i in range(0, len(num)):
#         sum += int(num[i])*math.pow(8, i)
#     print(int(sum))

# A14
# n = 100
# count = 0
# for i in range(0, n+1, 5):
#     remains = n - i
#     count += int(remains/2) + 1
# print(count)

# A15
# string = list(input())
# point = 0
# total = 0
# for s in string:
#     if s == 'X':
#         point = 0
#     else:
#         point += 1
#         total += point
# print(total)

# A16
# import math
# lst = list(range(10, 28))  # 所有结果是4的：10，11，12，，，，27
# n = int(input())
# if n == 0:
#     print(0)
# else:
#     count = 1
#     num = 1
#     total = num
#     while total < n:
#         count += 1
#         num *= 3
#         total += num
#     print(count)
