import collections
from collections import namedtuple, Counter, OrderedDict

# 1
# num = list(map(int, input().split()))
# x, y = num[0], num[1]
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(x=x, y=y)
# print(p)

# 2
# s = list(input())
# s = list(map(int, s))
# counter = Counter(s)
# result = []
# for i in range(0, 10):
#     if i in counter.keys():
#         result.append(counter.get(i))
#     else:
#         result.append(0)
# print(*result)

# 3
# n = int(input())
# item_list = input().split()
# counter = Counter(item_list)
# 先按出现次数排序，降序，取负号升序；再按name以字典序排序，升序
# counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
# for item in counter:
#     print(item[0], item[1])

# 4
# s = input().lower()
# lst = [i for i in s if i.isalpha()]
# counter = Counter(lst)
# counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
# # counter = sorted(counter.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
# for item in counter:
#     print(item[0], item[1])

# 5
# from collections import UserList
#
#
# class AutoList(UserList):
#
#     def __setitem__(self, i, item):
#         # TODO
#         if i < len(self.data):
#             self.data[i] = item
#         else:
#             self.data = self.data + [0]*(i-len(self.data)) + [item]
#
#     def __getitem__(self, i):
#         # TODO
#         if i < len(self.data):
#             return self.data[i]
#         else:
#             self.data = self.data + [0]*(i-len(self.data)+1)
#             return 0
#
# L = AutoList(eval(input()))
# i, x = map(int, input().split())
# L[i] = x
# print(L)
# print(L[int(input())])


# 6
from collections import ChainMap, OrderedDict

def pop_item(chain_map, item):
    try:
        chain_map.pop(item)
    except:
        pop_item(chain_map.parents, item)
    finally:
        return chain_map


default = eval(input())
user = eval(input())
workspace = eval(input())
op_1 = input()
op_2 = input()
config_tree = ChainMap(workspace, user, default)
config_tree = pop_item(config_tree, op_1)
print(config_tree[op_1])

config_tree = pop_item(config_tree, op_2)
print(config_tree[op_2])

# 7
# from collections import deque
# nums = list(map(int, input().split()))
# k = int(input())
# window = deque(nums[:k], k)
# result = []
# for i in range(k, len(nums)):
#     result.append(max(window))
#     window.append(nums[i])
# result.append(max(window))
# print(*result)


