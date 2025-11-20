# py里面关于位置参数和关键字参数

# 顺序：位置参数、可变位置参数、关键字参数、可变关键字参数

def func(a, b, *args, c=10, d=20, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("d:", d)
    print("kwargs:", kwargs)


# func(1, 2, 3, 4, 5, c=30, e=50, f={
#     'x': 100,
#     'y': 200
# })

# 可选参数（在python里面没有真正意义上的可选参数，可以通过给参数设置默认值来实现类似可选参数的效果）


def greet(name, greeting=None):
    if greeting is None:
        print("检测到未提供问候语，使用默认问候语。")
        greeting = "Hello"
    else:
        print("使用提供的问候语。")


# greet("Alice")  # 使用默认问候语
# greet("Bob", "Hi")  # 使用自定义问候语

my_list = []

# print("检验my_list是否为空：", not my_list)  # True if empty, False if not empty


def is_not_empty(data_list: list) -> bool:
    """
    @param data_list: 要检查的数组
    @return: 如果数组不为空返回True，否则返回False

    """
    if not data_list:
        return True
    else:
        return False


# print("检验my_list是否为空：", is_not_empty(my_list))


# 使用not来检查各种空值
a = ''
if not a:
    print("a是一个空字符串")
else:
    print("a不是一个空字符串")


b = {}
if not b:
    print("b是一个空字典")
else:
    print("b不是一个空字典")

c = [1, 2, 3,]
if not c:
    print("c是一个空数组")
else:
    print("c不是一个空数组")

d = 0
if not d:
    print("d是0")
else:
    print("d不是0")
