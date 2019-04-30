# 1 略

# 2
# a = eval(input())
# print(isinstance(a, (int, float)))

# 3
# class A:
#     pass
#
# class B(A):
#     pass
#
# name = globals()[input()]
# print(issubclass(name, A))

# 4
# class A:
#     def __init__(self, message):
#         self.message = message
#
#     # TODO
#     def __call__(self):
#         print(self.message)
#
#
# a = A(input())
#
# print(callable(A))
# print(callable(a))
# a()

# 5
# class A:
#     def __init__(self):
#         self.n = 1
#
#     def add(self, m):
#         # TODO
#         self.n += m
#
# class B(A):
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         # TODO
#         super().add(m)
#
# class C(A):
#     def __init__(self):
#         self.n = 2
#
#     def add(self, m):
#         # TODO
#         super().add(m)
#
# class D(B, C):
#     def __init__(self):
#         self.n = 3
#
#     def add(self, m):
#         super().add(m)
#         self.n += m
#
# d = D()
# d.add(int(input()))
# print(d.n)

# 6
# class Student:
#     def __getattr__(self, name):
#         if name == 'info':
#             return '\n'.join([
#                 '姓名: ' + getattr(self, 'name'),
#                 '学号: ' + getattr(self, 'sno'),
#                 '年级: ' + getattr(self, 'grade')])
#         return ''
#
#
# name, sno, grade = input().split()
# student = Student()
# student.__setattr__('name', name)
# student.__setattr__('sno', sno)
# student.__setattr__('grade', grade)
# print(student.__getattr__('info'))

# 7
class Complex(complex):
    def __init__(self, real, imag):
        complex.__init__(real, imag)

    def __repr__(self):
        return '{:.1f} + {:.1f}j'.format(self.real, self.imag)

    def __str__(self):
        return 'Complex(real={:.1f}, imag={:.1f})'.format(self.real, self.imag)


real, imag = map(int, input().split())
comp = Complex(real, imag)
print(repr(comp))
print(str(comp))
print(comp)

# class Complex(complex):
#     def __init__(self, real, imag):
#         complex.__init__(real, imag)
#
#
# real, imag = map(int, input().split())
# comp = Complex(real, imag)
# print(str(comp))
# print(repr(comp))
# print(comp)