

# 如何使用py声明一个对象


class User:
    def __init__(self):
        self.name = "Default Name"
        self.age = 0

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


# 创建一个对象实例
user = User()
user.set_name('Jie')
user.set_age(25)
print(user.get_info())
