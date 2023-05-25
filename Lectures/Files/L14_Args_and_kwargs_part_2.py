# ----------------------------
def show_multiply(*args):
    res = args[0]
    for num in args[1:]:
        res *= num
        print(res)

def show_divide(*args):
    res = args[0]
    for num in args[1:]:
        res /= num
        print(res)

show_multiply(4, 5, 6, 7, 8, 9, 10)
# 20
# 120
# 840
# 6720
# 60480
# 604800
# 604800

show_multiply(10, 9, 8, 7, 6, 5, 4)
# 90
# 720
# 5040
# 30240
# 151200
# 604800
# 604800

show_divide(4, 5, 6, 7, 8, 9, 10)
# 0.8
# 0.13333333333333333
# 0.019047619047619046
# 0.0023809523809523807
# 0.0002645502645502645
# 2.6455026455026453e-05
# 2.6455026455026453e-05

show_divide(10, 9, 8, 7, 6, 5, 4)
# 1.1111111111111112
# 0.1388888888888889
# 0.019841269841269844
# 0.003306878306878307
# 0.0006613756613756614
# 0.00016534391534391536
# 0.00016534391534391536

# ----------------------------
def print_args_1(*args):
    for arg in args:
        print(arg)

print_args_1(1,2,3)
# 1
# 2
# 3

print_args_1() # no output

def print_args_2(*args):
    first_arg = args[0]
    for arg in args:
        print(arg)

print_args_2(1,2,3)
# 1
# 2
# 3

print_args_2()
# IndexError: tuple index out of range

# ----------------------------
def print_values_1(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

def print_values_2(name, surname, **kwargs):
    print(f"Name, Surname: {name} {surname}")
    for key, value in kwargs.items():
        print(key, value)

print_values_1(name="John", surname="Johnes", gender="male", age="30",
             things=["cell phone", "earphones", "bag"])
# name John
# surname Johnes
# gender male
# age 30
# things ['cell phone', 'earphones', 'bag']

print_values_2(name="John", surname="Johnes", gender="male", age="30",
             things=["cell phone", "earphones", "bag"])
# Name, Surname: John Johnes
# gender male
# age 30
# things ['cell phone', 'earphones', 'bag']
