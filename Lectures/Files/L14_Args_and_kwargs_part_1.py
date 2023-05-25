# ----------------------------
# * - the single asterisk unpacking operator.
# An asterisk * denotes iterable unpacking. Its operand must be an ITERABLE.
# Can be used on any iterable that Python provides.

# ** - the duoble asterisk unpacking operator.
# A double asterisk ** denotes dictionary unpacking. Its operand must be a MAPPING.
# Can be used only on a dictionary.

# ----------------------------
print(*2)
# TypeError: print() argument after * must be an iterable, not int

x = 2
print(*x)
# TypeError: print() argument after * must be an iterable, not int

xs = (1, 2, 3, 4)
ys = [1, 2, 3, 4]

print(*xs)
# 1 2 3 4

print(*ys)
# 1 2 3 4

print(1, 2, 3, 4)
# 1 2 3 4

type(*xs)
# TypeError: type() takes 1 or 3 arguments

type(*ys)
# TypeError: type() takes 1 or 3 arguments

type(1, 2, 3, 4)
# TypeError: type() takes 1 or 3 arguments

# ----------------------------
print(**[1, 2, 3, 4])
# TypeError: print() argument after ** must be a mapping, not list

xs = (1, 2, 3, 4)
print(**xs)
# TypeError: print() argument after ** must be a mapping, not tuple

ys = {"a": 1, "b": 2, "c": 3, "d": 4}

print(*ys)
# a b c d

print("a", "b", "c", "d")
# a b c d

print(**ys)
# TypeError: 'a' is an invalid keyword argument for print()

type(**ys)
# TypeError: type() takes 1 or 3 arguments

type(a=1, b=2, c=3, d=4)
# TypeError: type() takes 1 or 3 arguments

# --------------
def print_kwargs(**kwargs):
    print(kwargs.keys())
    print(kwargs.items())

print_kwargs(**ys)
# dict_keys(['a', 'b', 'c', 'd'])
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

print_kwargs(a=1, b=2, c=3, d=4)
# dict_keys(['a', 'b', 'c', 'd'])
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# ----------------------------
# The function accepts any number of positional arguments.
#
# It takes all the arguments it receives and PACKS them all into a single
# iterable object (a tuple) named args.
#
# "args" is just a name
#
# PACKING is performed like so:
#
# `*` is the iterable unpacking operator.
# `args` in `*args` is an iterable to be unpacked (a tuple)    | `args`  match `(1, 2, 3, "a", "b", "c")`
# `*args` is an unpacked tuple, i.e. positional arguments      | `*args` match `1, 2, 3, "a", "b", "c"` in `fun_with_args(1, 2, 3, "a", "b", "c")`
#
# In this way, positional arguments match `*args`, and `args` match a tuple,
# into which the positional arguments are PACKED.
#
def fun_with_args(*args):
    print(args)
    print((1, 2, 3, "a", "b", "c"))
    print(type(args))
    print(type((1, 2, 3, "a", "b", "c")))
    print("----------------------")
    print(*args)
    print(1, 2, 3, "a", "b", "c")
    print(*args,)
    print(1, 2, 3, "a", "b", "c")
    print("-----------")
    print(*args, sep="|")
    print(1, 2, 3, "a", "b", "c", sep="|")
    print("-----------")
    #print(type(*args))              # TypeError: type() takes 1 or 3 arguments
    print("----------------------")
    #print((*args))                  # SyntaxError: cannot use starred expression here
    print("-----------")
    print((*args,))
    print((1, 2, 3, "a", "b", "c"))
    print(type((*args,)))
    print(type((1, 2, 3, "a", "b", "c")))
    print("-----------")
    print([*args])
    print([1, 2, 3, "a", "b", "c"])
    print(type([*args]))
    print(type([1, 2, 3, "a", "b", "c"]))
    print("----------------------")
    print(*[*args])
    print(*args)
    print("-----------")
    print(*(*args,))
    print(*args)
    print("----------------------")
    #print(**args)                   # TypeError: print() argument after ** must be a mapping, not tuple
    print("----------------------")

fun_with_args(1, 2, 3, "a", "b", "c")

# ----------------------------
# The function accepts any number of keyword arguments.
#
# It takes all the keyword arguments it receives and PACKS them all into a
# single mapping object (a dictionary) named kwargs.
#
# "kwargs" is just a name
#
# PACKING is performed like so:
#
# `**` is the mapping unpacking operator.
# `kwargs` in `*kwargs` is a mapping to be unpacked (a dictionary)    | `kwargs`   match `{"d": "e", "f": "g", "h": 4}`
# `**kwargs` is an unpacked dicionary, i.e. keyword arguments         | `**kwargs` match `d="e", f="g", h=4` in `fun_with_kwargs(d="e", f="g", h=4)`
#
# In this way, keyword arguments match `**kwargs`, and `kwargs` match a
# dictionary, into which the keyword arguments are PACKED.
#
def fun_with_kwargs(**kwargs):
    print(kwargs)
    print({"d": "e", "f": "g", "h": 4})
    print(type(kwargs))
    print(type({"d": "e", "f": "g", "h": 4}))
    print("----------------------")
    print(*kwargs)
    print("d", "f", "h")
    print("-----------")
    print(*kwargs, sep="|")
    print("d", "f", "h", sep="|")
    print("----------------------")
    print([*kwargs])
    print(["d", "f", "h"])
    print(type([*kwargs]))
    print(type(["d", "f", "h"]))
    print("----------------------")
    print((*kwargs,))
    print(("d", "f", "h"))
    print(type((*kwargs,)))
    print(type(("d", "f", "h")))
    print("----------------------")
    #print(**kwargs)       # TypeError: 'd' is an invalid keyword argument for print()
    #print(type(**kwargs)) # TypeError: type() takes 1 or 3 arguments
    print("----------------------")
    print(kwargs.keys())
    print(kwargs.items())
    print("----------------------")

fun_with_kwargs(d="e", f="g", h=4)
