import re
# 1
n = int(input())
for i in range(n):
    lst = input().split()
    target, content = lst[0], lst[1]
    pattern = re.compile(target)
    result = pattern.match(content)
    if result:
        print(result.span())
        break
    else:
        print(None)


# 2
# n = int(input())
# for i in range(n):
#     one_line = input().split()
#     target, content = one_line[0], one_line[1]
#     pattern = re.compile(target)
#     result = pattern.search(content)
#     if result:
#         print(result.span())
#     else:
#         print(None)

# 3
# n = int(input())
# for i in range(n):
#     content = input()
#     phone_num = re.sub(r'\D', '', content)
#     print(phone_num)

# 4
# def double(matched):
#     a = int(matched.group())
#     return str(a*2)
#
#
# n = int(input())
# for i in range(n):
#     content = input()
#     phone_num = re.sub(r'\d+', double, content)
#     print(phone_num)

# pattern = re.compile('abc')
# result = re.findall(r'\d*', 'A23G4HFD567')
# print(result)

# 5
# n = int(input())
# for i in range(n):
#     content = input()
#     start, end = tuple(map(int, input().split()))
#     pattern = re.compile(r'\d+')
#     result = pattern.findall(content, start, end)
#     print(result)

# 6
# n = int(input())
# for i in range(n):
#     nums = input()
#     pattern = re.compile(r'[1-9]\d{4}\d*')
#     result = pattern.findall(nums)
#     print(result)

# 7
# n = int(input())
# for i in range(n):
#     target = input()
#     pattern = input()
#     result = re.search(pattern, target)
#     print(bool(result))
