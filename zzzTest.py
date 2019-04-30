# l = [1, 2, 3]
# l2 = l + [0]*3
# print(l2)
# from collections import ChainMap
# a = ChainMap({'a': 1, 'b': 2}, {'a': 0, 'c': 3, "d": 4})
# a.parents.pop('a')
# print(a['e'])

import re
a = 'www'
b = 'asjdanswwwnsasnwww'
result = re.search(a, b)
print(result.span())
