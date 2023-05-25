# ----------------------------
# Tuple
# ----------------------------
t = (1,2)
# t = (1,2)
t = (1,2,1)
# t = (1,2,1)
type(t)
# <class 'tuple'>
t.count(1)
# 2
t.index(2)
# 1
t.index(1)
# 0

# ----------------------------
# Set
# ----------------------------
s = {1, 2}
# s = {1, 2}
type(s)
# <class 'set'>
s = {"a": 1, "b": 2}
type(s)
# <class 'dict'>

s = {1, 2}
# s = {1, 2}
s.add(3)
# s = {1, 2, 3}
el = s.pop()
# el = 1
# s = {2, 3}
s.remove(3)
# s = {2}

# ----------------------------
# tuple(), set()
# ----------------------------
# tuple (Sequence type), set (Set type)
# collections.Counter Class (Multiset type)
# t = tuple(1,2,3)  <-- uncomment to see the error
# ERROR: 1 arg max
# s = set(1,2,3)    <-- uncomment to see the error
# ERROR: 1 arg max

t = tuple((1,2,3))
# t = (1, 2, 3)
s = set((1,2,3))
# s = {1, 2, 3}

# ----------------------------------
# Element order & repeating elements
# ----------------------------------
t = tuple((1,2,1))
# t = (1, 2, 1)
# ^---- Sequence type - Element order is important
t = tuple((2,1,1))
# t = (2, 1, 1)
# ^---- Sequence type - Element order is important
# (Element order is important in all other sequence types as well)

s = set((1,2,1))
# s = {1, 2}
# ^---- Adds only once, ignores same elements (because it's a set, not a multiset)
s = set((2,1,1))
# s = {1, 2} # same result
# ^---- For sets (and multisets) element order is not important

t1 = (1,2,1)
t2 = (1,2,1)
t1 == t2
# True

t1 = (1,2,1)
t2 = (1,1,2)
t1 == t2
# False

s1 = set((1,2,1))
s2 = set((2,1,1))
s1 == s2
# True

(1,2) == {1,2}
# False
(1,2) == tuple({1,2})
# True
set((1,2)) == {1,2}
# True

# ----------------------------
# Indexing tuples and sets
# ----------------------------
t = (1,2,3)
t[0]
# 1
t[1]
# 2
t[-1]
# 3

s = {1,2,3}
# s[0]   <-- uncomment to see the error
# ERROR: 'set' object is not subscriptable
# s[2]   <-- uncomment to see the error
# ERROR: ... # we can't index a set, since the order of its elements is not important

# --------------------------------------
# Mutability of tuples, sets and strings
# --------------------------------------
t = (1,2,3)
# t[0] = 9    <-- uncomment to see the error
# ERROR: 'tuple' object does not support item assignment
# (because it's immutable)

t1 = (1,2)
t2 = (3,)
t1 + t2
# (1, 2, 3)
t3 = t1 + t2
# t3 = (1, 2, 3)
t1
# t1 = (1, 2)
t2
# t2 = (3,)
id_t1_before = id(t1)
t1 = t1 + t2
# t1 = (1, 2, 3)
id_t1_after = id(t1)
id_t1_before != id_t1_after
# True

s = {1,2,3}
# s[0] = 4    <-- uncomment to see the error
# ERROR: 'set' object does not support item assignment
# (because we can't index a set)
s.add(4)
# s = {1,2,3,4} <- s is the same object

s = "Hello"
# s[0] = "W"    <-- uncomment to see the error
# ERROR: 'str' object does not support item assignment
# s.append("World")    <-- uncomment to see the error
# ERROR: 'str' object has no attribute 'append'
# see Python String Methods at:
# https://www.w3schools.com/python/python_ref_string.asp

s1 = "Hello"
s2 = "World"
s1 + s2
# 'HelloWorld'
s1
# 'Hello'
s2
# 'World'
s1 = s1 + s2
# s1 is a new object now

# ----------------------------
# dict items() method
# ----------------------------

ages = {"John": 20, "Andrew": 34, "Laura": 25}
for key, value in ages.items():
    key, value
...
a_tuple = ('Andrew', 20)
# for key, value in a_tuple:    <-- uncomment to see the error
#    key, value
# ERROR: too many values to unpack (expected 2)
