
class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating a new Person instance")
        print("cls:", cls)
        print("args:", args)
        print("kwargs:", kwargs)

        instance = super(Person, cls).__new__(cls)
        return instance

    def __init__(self, name, age):
        print("Initializing a new Person instance")
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def is_adult(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False


person_one = Person("Jack", 20)

print(person_one.greet())

print(person_one.is_adult())
