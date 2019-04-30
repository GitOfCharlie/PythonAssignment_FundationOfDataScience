# 1
# lst = eval(input())
# print(max(lst), min(lst))

# 2
# lst = eval(input())
# print(sum(lst))

# 3
# a1, n, d = tuple(map(int, input().split()))
# bias = -1 if d < 0 else 1
# sequence = range(a1, a1 + (n-1)*d + bias, d)
# print(*sequence)

# 4
# names = input().split()
# records = enumerate(names, start=10001)
# for record in records:
#     print(record[0], record[1])

# 5
# import math
# def is_sqr(n):
#     a = int(math.sqrt(n))
#     return n == a**2
#
#
# n, m = tuple(map(int, input().split()))
# nums = list(range(n, m+1))
# results = filter(is_sqr, nums)
# print(*results)

# 6
# n = int(input())
# stu = []
# for i in range(n):
#     info = input().split(',')
#     name = info[0]
#     scores = info[1:]
#     scores = map(int, ['0' if one_score == '' else one_score for one_score in scores])
#     is_fail = [one_score < 60 for one_score in scores]
#     if any(is_fail):
#         stu.append(name)
# print(stu)

# 7
# n = int(input())
# stu = []
# for i in range(n):
#     info = input().split(',')
#     name = info[0]
#     scores = info[1:]
#     if all(scores):
#         stu.append(name)
# print(stu)

# 8
# names = input().split()
# scores = list(map(int, input().split()))
# ages = list(map(int, input().split()))
# records = []
# for i in range(len(names)):
#     records.append((names[i], scores[i], ages[i]))
# print(sorted(records, key=lambda x: x[1]))
# print(sorted(records, key=lambda x: x[2]))

# 9
# storages = input().split(',')
# commodity = input().split(',')
# zipped = zip(storages, commodity)
# for one in zipped:
#     print(one)

# 10
# records = eval(input())
# storage = [one[0] for one in records]
# commodity = [one[1] for one in records]
# print(storage)
# print(commodity)