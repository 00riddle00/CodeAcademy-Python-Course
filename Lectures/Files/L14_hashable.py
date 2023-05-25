# ----------------------------
# Hashes remain the same in other Python Shell sessions.

hash(False)
# 0

hash(True)
# 1

hash(0)
# 0

hash(1)
# 0

hash(2)
# 2

hash(3)
# 3

hash("a")
# 4237317445913395571

hash("abc")
# 3003167503646137946

# ----------------------------
# Tuple is hashable if all its elements are hashable
tup1 = tuple([1, 2, 3])
tup1
# (1, 2, 3)

hash(tup1)
# 529344067295497451

tup2 = tuple([1, 2, "abc"])
tup2
# (1, 2, 'abc')

hash(tup2)
# 4512050901658190381

tup3 = tuple([1, 2, 3, [4, 5]])
tup3
# (1, 2, 3, [4, 5])

hash(tup3)
# TypeError: unhashable type: 'list'

# ----------------------------
# Set is not hashable, but all its elements must be hashable

set1 = {1, 2, 3}
set1
# {1, 2, 3}

hash(set1)
# TypeError: unhashable type: 'set'

set2 = {1, 2, 3, []}
# TypeError: unhashable type: 'list'

# ----------------------------
# Function is hashable
>>> hash
# <built-in function hash>

>>> type(hash)
# <class 'builtin_function_or_method'>

hash(hash)
# 669582

# ----------------------------
# Hashable - a characteristic of a Python object to indicate whether the object
# has a hash value, which allows the object to server as a key in a dictionary
# or an element in a set.

dict1 = {"a": 1, "b": 2}
dict1
# {'a': 1, 'b': 2}

dict2 = {[1,2]: 3, "b": 2}
# TypeError: unhashable type: 'list'

# Function can be a dict key:
dict3 = {hash: 1, "b": 2}
dict3
# {<built-in function hash>: 1, 'b': 2}

# or an element in a set
set3 = {1, hash, 2}
set3
# {1, 2, <built-in function hash>}

# ----------------------------
# Hashability is linked to equality (not identity)

i_1 = 10
i_2 = 10

id(i_1)
# 139781819790600
id(i_2)
# 139781819790600

hash(i_1)
# 10
hash(i_2)
# 10

type(hash(i_1))
# <class 'int'>

id(hash(i_1))
# 139781819790600

id(hash(i_2))
# 139781819790600

hash(i_1) == hash(i_2)
# True
hash(i_1) is hash(i_2)
# True

i_1 == i_2
# True

i_1 is i_2
# True

# -------------
i_3 = 1000
i_4 = 1000

id(i_3)
# 139781803142032
id(i_4)
# 139781803142384

hash(i_3)
# 1000
hash(i_4)
# 1000

id(hash(i_3))
# 139781803138928
id(hash(i_4))
# 139781803142416

hash(i_3) == hash(i_4)
# True
hash(i_3) is hash(i_4)
# False

i_3 == i_4
# True

i_3 is i_4
# False
