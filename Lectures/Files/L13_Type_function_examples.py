xs = (1, 2)

type(xs)
# <class 'tuple'>

type(tuple)
# <class 'type'>

tuple is type(tuple)
# False

tuple == type(tuple)
# False

type(xs) == tuple
# True

type((1, 2))
# <class 'tuple'>

tuple()
# ()

type(type)
# <class 'type'>

def fun_1():
    print("Hi!")

def fun_2():
    return None

def fun_3(x):
    print(x)

def fun_4(x):
    return x + x

type(fun_1)
# <class 'function'>

type(fun_1())
# Hi!
# <class 'NoneType'>

type(fun_2())
# <class 'NoneType'>

type(fun_3(8))
# 8
# <class 'NoneType'>

type(fun_4(8))
# <class 'int'>

a = fun_4(8)
type(a)
# <class 'int'>

callable(fun_1)
# True

callable(fun_1())
# Hi!
# False

callable(fun_3)
# True

callable(fun_3(4))
# 4
# False
