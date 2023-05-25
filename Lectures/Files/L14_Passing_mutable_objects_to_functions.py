# ----------------------------
# Modifying global mutable objects (lists) inside a function.

source = [1, 2, 3]
destination = []

print("source:", source)
# source: [1, 2, 3]
print("destination:", destination)
# destination: []
print()

def fun_1(src, dest):
    while src:
        el = source.pop()
        destination.append(el)

fun_1(source, destination)

print("source: ", source)
# source:  []
print("destination: ", destination)
# destination:  [3, 2, 1]

# ----------------------------
# Modifying global mutable objects (lists) inside a function,
# through function parameters (= formal arguments)

source = [1, 2, 3]
destination = []

print("source:", source)
# source: [1, 2, 3]
print("destination:", destination)
# destination: []
print()

def fun_2(src, dest):
    while src:
        el = src.pop()
        dest.append(el)

fun_2(source, destination)

print(src)
# NameError: name 'src' is not defined

print("source: ", source)
# source:  []
print("destination: ", destination)
# destination:  [3, 2, 1]

# ----------------------------
# Printing IDs

source = [1, 2, 3]
destination = []

print("id_source", id(source))
# id_source 140544709813696
print("id_destination", id(destination))
# id_destination 140544709812800
print()

def fun_3(src, dest):
    print("id_source", id(source))
    print("id_destination", id(destination))
    print()

    print("id_src", id(src))
    print("id_dest", id(src))
    print()

fun_3(source, destination)
# id_source 140544709813696
# id_destination 140544709812800

# id_src 140544709813696
# id_dest 140544709813696

# ----------------------------
source = [1, 2, 3]
destination = []

print("id_source", id(source))
# id_source 140544709797056
print("id_destination", id(destination))
# id_destination 140544709813696
print()

def fun_4():
    print("id_source", id(source))
    print("id_destination", id(destination))
    print()

    # This is how parameters took the value of arguments:
    src = source       # just a simple assignment (= relabeling), still the same object
    dest = destination # just a simple assignment (= relabeling), still the same object

    print("id_src", id(src))
    print("id_dest", id(src))

fun_4()
# id_source 140544709797056
# id_destination 140544709813696

# id_src 140544709797056
# id_dest 140544709797056

# ----------------------------
# Reassignment - only the VALUE from "src"/"source" is used.

source = [1, 2, 3]
destination = []

print("source:", source)
# source: [1, 2, 3]
print("destination:", destination)
# destination: []
print()

def fun_5(src, dest):
    print(id(src))
    src = src + dest
    print(id(src))

    while src:
        el = src.pop()
        dest.append(el)

    print("src: ", src)

fun_5(source, destination)
# 140544709812800
# 140544709813696
# src:  []

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  [3, 2, 1]

# ----------------------------
# Simple assignment

list_a = [1, 2, 3]
id(list_a)
# 140544709813696

list_b = list_a
id(list_b)
# 140544709813696

# ----------------------------
# What do we do when we want to create a new object?

list_a = [1, 2, 3]

# slice gives a new object
list_b = list_a[:] # same as list_a[0:3]

list_a
# [1, 2, 3]

list_b
# [1, 2, 3]

id(list_a)
# 140544709794688

id(list_b)
# 140544709524928

# ----------------------------
# Passing a list to a function and ensuring it is not modified inside it
source = [1, 2, 3]
destination = []

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  []
print()

def fun_6(src, dest):
    while src:
        el = src.pop()
        dest.append(el)

fun_6(source[:], destination)

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  [3, 2, 1]

# ----------------------------
# Ensuring "src" is not modified from inside the function
source = [1, 2, 3]
destination = []

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  []
print()

def fun_7(src, dest):
    src = src[:]

    while src:
        el = src.pop()
        dest.append(el)

fun_7(source, destination)

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  [3, 2, 1]

# ----------------------------
# The dangers still exist
source = [1, 2, 3]
destination = []

print("source: ", source)
# source:  [1, 2, 3]
print("destination: ", destination)
# destination:  []
print()

def fun_8(src, dest):

    while src:
        el = src.pop()
        dest.append(el)

    source.pop() # <-- nothing still prevents us from doing that.

fun_8(source[:], destination)

print("source: ", source)
# source:  [1, 2]
print("destination: ", destination)
# destination:  [3, 2, 1]
