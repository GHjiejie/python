# 判断数据类型
a = 123
print(type(a))  # <class 'int'>

b = "Hello, World!"
print(type(b))  # <class 'str'>

c = [1, 2, 3, 4, 5]
print(type(c))  # <class 'list'>

d = (1, 2, 3, 4, 5)
print(type(d))  # <class 'tuple'>

e = {'a': 1, 'b': 2, 'c': 3}
print(type(e))  # <class 'dict'>

f = 3.14
print(type(f))  # <class 'float'>

g = True
print(type(g))  # <class 'bool'>

h = {1, 2, 3, 4, 5}
print(type(h))  # <class 'set'>

# 判断变量是否是某个特定类型
if isinstance(a, int):
    print("a是一个整数")

if isinstance(b, str):
    print("b是一个字符串")

if isinstance(c, list):
    print("c是一个列表")

if isinstance(d, tuple):
    print("d是一个元组")

if isinstance(e, dict):
    print("e是一个字典")

if isinstance(f, float):
    print("f是一个浮点数")

if isinstance(g, bool):
    print("g是一个布尔值")

if isinstance(h, set):
    print("h是一个集合")

# 使用type()函数和isinstance()函数的区别
# i = 10
# if type(i) == int:
#     print("i的类型是整数")
