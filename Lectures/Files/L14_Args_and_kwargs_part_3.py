
def fun(name, age, *args, **kwargs):
    print(f"Name: {name}, age: {age}")
    #
    for arg in args:
        print(f"arg: {arg}")
    #
    for identifier, expression in kwargs.items():
        print(f"Identifier: {identifier}")
        print(f"Expression: {expression}")

fun("John", 30)
# Name: John, age: 30

fun(age=30, name="John")
# Name: John, age: 30

fun(age=30, name="John", 1, 2, 3)
# SyntaxError: positional argument follows keyword argument

fun(1, 2, 3, age=30, name="John")
# TypeError: fun() got multiple values for argument 'age'

fun(30, "John", 1, 2, 3, four=4, five=5, six=6)
# Name: 30, age: John
# arg: 1
# arg: 2
# arg: 3
# Identifier: four
# Expression: 4
# Identifier: five
# Expression: 5
# Identifier: six
# Expression: 6

fun(30, "John", *[1, 2, 3], four=4, five=5, six=6)
# Name: 30, age: John
# arg: 1
# arg: 2
# arg: 3
# Identifier: four
# Expression: 4
# Identifier: five
# Expression: 5
# Identifier: six
# Expression: 6

fun(30, "John", [1, 2, 3], four=4, five=5, six=6)
# Name: 30, age: John
# arg: [1, 2, 3]
# Identifier: four
# Expression: 4
# Identifier: five
# Expression: 5
# Identifier: six
# Expression: 6

fun(30, "John", [1, 2, 3], {"four": 4, "five": 5, "six": 6})
# Name: 30, age: John
# arg: [1, 2, 3]
# arg: {'four': 4, 'five': 5, 'six': 6}

fun(30, "John", [1, 2, 3], **{"four": 4, "five": 5, "six": 6})
# Name: 30, age: John
# arg: [1, 2, 3]
# Identifier: four
# Expression: 4
# Identifier: five
# Expression: 5
# Identifier: six
# Expression: 6

