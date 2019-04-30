# 1
# n = eval(input())
# print(abs(n))

# 2
# a, b = tuple(map(int, input().split()))
# result = divmod(a, b)
# print(*result)

# 3
# a, n = tuple(map(int, input().split()))
# result = pow(a, 1/n)
# print(round(result, 2))

# 4
# asc = int(input())
# print(chr(asc))

# 5
# c1, c2 = tuple(input().split())
# diff = abs(ord(c1) - ord(c2))
# print(diff)


# 6 处理所有非ascii字符
# string = input()
# invalid_char = [ascii(c) for c in string if ord(c) >= 128]
# print(" ".join(invalid_char).replace("'", ""))

# 7 二进制、八进制、十六进制
# n = int(input())
# print(bin(n), oct(n), hex(n))

# 8 二进制转十进制eval()
# n = eval(input())
# print(n)

# 9
# calcu = eval(input())
# print(calcu)

# 10
# command = input()
# exec(command)