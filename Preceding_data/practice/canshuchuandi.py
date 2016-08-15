def f(a, b, c):
    return a+b+c

print(f(1, 2, 3))

print(f(c=3, b=2, a=1))

print(f(1, c=3, b=2))


def f1(a, b, c=10):
    return a+b+c
print(f1(3, 2))
print(f1(3, 2, 1))


def func(*name):
    print(type(name))
    print(name)
func(5, 6, 7, 1, 2, 3)


def func(**dict):
    print(type(dict))
    print(dict)
func(a=1, b=9)
func(m=2, n=1, c=11)


def func2(a, b, c):
    print(a, b, c)
args = (1, 3, 4)
func2(*args)


dict2 = {'a': 1, 'b': 2, 'c': 3}
func(**dict2)
