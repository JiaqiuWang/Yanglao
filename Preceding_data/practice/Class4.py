from random import choice
COLORS = ['Brown', 'Black', 'Golden']


class Animal(object):

    def __init__(self, color):
        self.color = color

    @classmethod
    def make_baby(cls):
        color = choice(COLORS)
        print("cls", cls)
        return cls(color)

    @staticmethod
    def speak():
        print("Rora")


class Dog(Animal):

    @staticmethod
    def speak():
        print("Bark!")

    @classmethod
    def make_baby(cls):
        print("making dog baby!")
        print("cls", cls)
        return super(Dog, cls).make_baby()


class Cat(Animal):
    pass

d = Dog('Brown')
print(d.color)
pup = d.make_baby()
print("pup", pup)
print("pup.color:", pup.color)
