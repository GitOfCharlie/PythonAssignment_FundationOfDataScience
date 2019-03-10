# 1
# set1 = set(eval(input()))
# set2 = set(eval(input()))
# print(set1.issubset(set2))

# 2
# set1 = set(eval(input()))
# set2 = set(eval(input()))
# set3 = set1 & set2
# if len(set3) == 0:
#     print('None')
# else:
#     print(set3)

# 3
# set1 = set(eval(input()))
# set2 = set(eval(input()))
# set3 = set1 | set2
# print(set3)

# 4
# set1 = set(eval(input()))
# set2 = set(eval(input()))
# set3 = set1 - set2
# print(set3)

# 5
# dic = dict(eval(input()))
# newDict = {value: key for key, value in dic.items()}
# print(newDict)
# print(dic.items())

# 6
# dic = dict(eval(input()))
# maxAge = max(dic.values())
# for name in dic.keys():
#     if dic[name] == maxAge:
#         print(name)
#         break

# 7
# from collections import OrderedDict
# lst = eval(input())
# dic = OrderedDict({})
# for name, score in lst:
#     if score >= 90:
#         grade = 'A'
#     elif 80 <= score < 90:
#         grade = 'B'
#     elif 70 <= score < 80:
#         grade = 'C'
#     elif 60 <= score < 70:
#         grade = 'D'
#     else:
#         grade = 'E'
#     dic[name] = grade
# topStudents = []
# for name in dic.keys():
#     if dic[name] in ['A', 'B']:
#         topStudents.append(name)
# # print(dic)
# print('{', end='')
# printList = []
# for name, grade in dic.items():
#     printList.append("'{0}': '{1}'".format(name, grade))
# print(', '.join(printList) + '}')
# print(topStudents)
