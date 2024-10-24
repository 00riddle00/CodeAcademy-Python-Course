print("==============================================================")
print("Boolean type [IMMUTABLE]")
# https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# https://docs.python.org/3/library/functions.html#bool
print("==============================================================")

bool_0 = bool()  # Default value of bool type is 'False'
print(bool_0)

bool_1 = False
bool_2 = True

print(type(bool_0))
print(type(bool_1))
print(type(bool_2))

print("------------------------------")

bool_ex1 = bool(0)
bool_ex2 = bool("text")
#bool_ex3 = bool("") == False  # Not recommended (With Boolean type)
bool_ex4 = bool("") is False  # Recommended (With Boolean type)

print(bool_ex1)
print(bool_ex2)
#print(bool_ex3)
print(bool_ex4)

print("==============================================================")
print("The Null Object (None) [IMMUTABLE]")
# https://docs.python.org/3/library/stdtypes.html#the-null-object
print("==============================================================")

none_1 = None

print(none_1)
print(type(none_1))

print("==============================================================")
print("Numeric types (int [IMMUTABLE], float [IMMUTABLE], complex [IMMUTABLE])")
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
print("==============================================================")

print("int [IMMUTABLE]")
# https://docs.python.org/3/library/functions.html#int
print("-------------------------------------------------")

int_1 = int()  # Default value for int type is 0
int_2 = 0

print(type(int_1))
print(type(int_2))

print(int_1)
print(int_2)

print("------------------------------")

int_ex1 = int(0.5)
int_ex2 = int("3" * 3)
int_ex3 = int("2")
int_ex4 = int(True)
int_ex5 = int(False)

print(int_ex1)
print(int_ex2)
print(int_ex3)
print(int_ex4)
print(int_ex5)

print("-------------------------------------------------")
print("float [IMMUTABLE]")
# https://docs.python.org/3/library/functions.html#float
print("-------------------------------------------------")

float_1 = float()  # Default value for float type is 0.0
float_2 = 0.0

print(type(float_1))
print(type(float_2))

print(float_1)
print(float_2)

print("------------------------------")

float_ex1 = float("2.5")
float_ex2 = float(1 + 3)
float_ex3 = float(True)
float_ex4 = float(False)

print(float_ex1)
print(float_ex2)
print(float_ex3)
print(float_ex4)

print("-------------------------------------------------")
print("complex [IMMUTABLE]")
# https://docs.python.org/3/library/functions.html#complex
print("-------------------------------------------------")

complex_1 = complex()  # Default value for complex type is 0j
complex_2 = 0j

print(type(complex_1))
print(type(complex_2))

print(complex_1)
print(complex_2)

print("------------------------------")

complex_ex1 = complex("1")
complex_ex2 = complex("1+2j")
complex_ex3 = complex(2 + 4j)
complex_ex4 = complex(True + 2.5j)

print(complex_ex1)
print(complex_ex2)
print(complex_ex3)
print(complex_ex4)

print("==============================================================")
print("Text Sequence Type (str) [IMMUTABLE]")
print("Sequence - order is important")
print("Sequence - elements can repeat")
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# https://docs.python.org/3/library/functions.html#func-str
print("==============================================================")

str_1 = str()  # Default value for string type is ""
str_2 = ""

print(type(str_1))
print(type(str_2))

print(str_1)
print(str_2)

print("------------------------------")

str_ex1 = "Hello   World"
str_ex2 = "'foo' " "bar"
str_ex3 = str(10 + 5.5)
str_ex4 = str(bool(1))

print(str_ex1)
print(str_ex2)
print(str_ex3)
print(str_ex4)

print("==============================================================")
print("Sequence types (list [MUTABLE], tuple [IMMUTABLE], range [IMMUTABLE])")
print("Sequence - order is important")
print("Sequence - elements can repeat")
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
print("==============================================================")

print("list [MUTABLE]")
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/library/functions.html#func-list
print("-------------------------------------------------")

list_1 = list()  # Default value for list type is []
list_2 = []

print(type(list_1))
print(type(list_2))

print(list_1)
print(list_2)

print("------------------------------")

list_ex1 = list("abc")
list_ex2 = list(["a", "b", "c"])
list_ex3 = list([1, 2, 3])
list_ex4 = list([ [1, 2, 3], [4, 5, 6] ])
list_ex5 = list(x for x in [])
list_ex6 = list( (1, 2, 3) )
list_ex7 = list( set((1, 2, 3)) )
list_ex8 = ["a",]

print(list_ex1)
print(list_ex2)
print(list_ex3)
print(list_ex4)
print(list_ex5)
print(list_ex6)
print(list_ex7)
print(list_ex8)

print("-------------------------------------------------")
print("tuple [IMMUTABLE]")
# https://docs.python.org/3/library/stdtypes.html#tuple
# https://docs.python.org/3/library/functions.html#func-tuple
print("-------------------------------------------------")

tuple_1 = tuple()  # Default value for tuple is ()
tuple_2 = ()

print(type(tuple_1))
print(type(tuple_2))

print(tuple_1)
print(tuple_2)

print("------------------------------")

tuple_ex1 = tuple([1, 2, "a", [3, 4]])
tuple_ex2 = tuple((1, 2, 3))
tuple_ex3 = tuple("Hello")
tuple_ex4 = tuple(x for x in "abc")
tuple_ex5 = ("a", "b", "c", 2, [])
tuple_ex6 = "a", "b", "c", 2
tuple_ex7 = "a",
tuple_ex8 = ("a",)
tuple_ex8 = (("a",))

print(tuple_ex1)
print(tuple_ex2)
print(tuple_ex3)
print(tuple_ex4)
print(tuple_ex5)
print(tuple_ex6)
print(tuple_ex7)
print(tuple_ex8)
print(tuple_ex9)

print("-------------------------------------------------")
print("range [IMMUTABLE]")
# https://docs.python.org/3/library/stdtypes.html#range
# https://docs.python.org/3/library/functions.html#func-range
print("-------------------------------------------------")

range_1 = range(0)  # Empty range is FALSY
range_2 = range(0, 0)

print(type(range_1))
print(type(range_2))

print(range_1)
print(list(range_1))
print(range_2)
print(list(range_2))

print("------------------------------")

range_ex1 = range(10)  # range(0, 10)
range_ex2 = range(1, 10)
range_ex3 = range(3, 9, 2)
range_ex4 = range(10, 0, -1)
range_ex5 = range(-10, 11, 2)
range_ex6 = range(-10, -21, -5)

print(list(range_ex1))
print(list(range_ex2))
print(list(range_ex3))
print(list(range_ex4))
print(list(range_ex5))
print(list(range_ex6))

print("==============================================================")
print("Mapping Type (dict) [MUTABLE]")
print("dict - order is not important")
print("dict - elements (key-value pairs) cannot repeat")
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# https://docs.python.org/3/library/functions.html#func-dict
print("==============================================================")

dict_1 = dict()  # Default value for dict is {}
dict_2 = {}

print(type(dict_1))
print(type(dict_2))

print(dict_1)
print(dict_2)

print("------------------------------")

dict_ex1 = {"":""}
dict_ex2 = {"name": "John", "age": 36}
dict_ex3 = dict([("foo", 100), ("bar", 200)])
dict_ex4 = dict({("foo", 100), ("bar", 200)})
dict_ex5 = dict(foo=100, bar=200)
dict_ex6 = dict({"Name":"John"}, age=36)
dict_ex7 = dict({"one": 1, "three": 3}, two=2)

print(dict_ex1)
print(dict_ex2)
print(dict_ex3)
print(dict_ex4)
print(dict_ex5)
print(dict_ex6)
print(dict_ex7)

print("==============================================================")
print("Set types (set [MUTABLE], frozenset [IMMUTABLE])")
print("Set - order is not important")
print("Set - elements cannot repeat, as they do in a multiset")
# https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
print("==============================================================")

print("set [MUTABLE]")
# https://docs.python.org/3/library/functions.html#func-set
print("-------------------------------------------------")

set_1 = set()
set_2 = {x for x in []}

print(type(set_1))
print(type(set_2))

print(set_1)
print(set_2)

print("------------------------------")

set_ex1 = {""}
set_ex2 = {None}
set_ex3 = {"a",}
set_ex4 = {x for x in "abc"}
set_ex5 = {"apple", "banana", "cherry"}
set_ex6 = set("abc")
set_ex7 = set(["a", "b", "foo"])
set_ex8 = set(("a", "b", "foo"))

print(set_ex1)
print(set_ex2)
print(set_ex3)
print(set_ex4)
print(set_ex5)
print(set_ex6)
print(set_ex7)
print(set_ex8)

print("-------------------------------------------------")
print("frozenset [IMMUTABLE]")
# https://docs.python.org/3/library/functions.html#func-frozenset
print("-------------------------------------------------")

frozenset_1 = frozenset()
frozenset_2 = frozenset(x for x in [])

print(type(frozenset_1))
print(type(frozenset_2))

print(frozenset_1)
print(frozenset_2)

print("------------------------------")

frozenset_ex1 = frozenset({"apple", "banana", "cherry"})
frozenset_ex2 = frozenset(("a",))
frozenset_ex3 = frozenset("abc")
frozenset_ex4 = frozenset(set("abc"))
frozenset_ex5 = frozenset(["a", "b", 2])

print(frozenset_ex1)
print(frozenset_ex2)
print(frozenset_ex3)
print(frozenset_ex4)
print(frozenset_ex5)

print("==============================================================")
print("Binary Sequence Types (bytes [IMMUTABLE], bytearray [MUTABLE], memoryview [MUTABLE])")
print("Sequence - order is important")
print("Sequence - elements can repeat")
# https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
print("==============================================================")

print("bytes [IMMUTABLE]")
# https://docs.python.org/3/library/functions.html#func-bytes
print("-------------------------------------------------")

bytes_1 = bytes()
bytes_2 = b""

print(type(bytes_1))
print(type(bytes_2))

print(bytes_1)
print(bytes_2)

print("------------------------------")

bytes_ex1 = b"Hello"
bytes_ex2 = bytes(10)
bytes_ex3 = bytes(range(20))
bytes_ex4 = b"still allows embedded 'single' quotes"
bytes_ex5 = bytes([1,2,3])

print(bytes_ex1)
print(bytes_ex2)
print(bytes_ex3)
print(bytes_ex4)
print(bytes_ex5)

print("-------------------------------------------------")
print("bytearray [MUTABLE]")
# https://docs.python.org/3/library/functions.html#func-bytearray
print("-------------------------------------------------")

bytearray_1 = bytearray()
bytearray_2 = bytearray(0)

print(type(bytearray_1))
print(type(bytearray_2))

print(bytearray_1)
print(bytearray_2)

print("------------------------------")

bytearray_ex1 = bytearray(5)
bytearray_ex2 = bytearray(b"Hello!")
bytearray_ex3 = bytearray(range(10))
bytearray_ex4 = bytearray([1,2,3])

print(bytearray_ex1)
print(bytearray_ex2)
print(bytearray_ex3)
print(bytearray_ex4)

print("-------------------------------------------------")
print("memoryview [MUTABLE]")
# https://docs.python.org/3/library/functions.html#func-memoryview
print("-------------------------------------------------")

memoryview_1 = memoryview(bytes())
memoryview_2 = memoryview(b"")

print(type(memoryview_1))
print(type(memoryview_2))

print(memoryview_1)
print(memoryview_2)

print("------------------------------")

memoryview_ex1 = memoryview(bytes(5))
memoryview_ex2 = memoryview(b"abcefg")
memoryview_ex3 = memoryview(bytearray(b"abc"))
memoryview_ex4 = memoryview(bytes(1,))

print(memoryview_ex1)
print(memoryview_ex2)
print(memoryview_ex3)
print(memoryview_ex4)
