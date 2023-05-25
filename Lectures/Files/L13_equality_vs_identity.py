# ----------------------------
True is True
# True

True is not False
# True

True is (not False)
# True

bool(2)
# True

True is bool(2)
# True

bool(2) is True
# True

id(True)
# 140566402101344
# ^-- different ID in a new Python Shell session.

id(False)
# 140566402100896

id(bool(2))
# 140566402101344

True == True
# True
# ^-- Not recommended

True == bool(2)
# True
# ^-- Not recommended

True != False
# True
# ^-- Not recommended

# ----------------------------
x = 200
if x == 200:
    print("x == 200!")
# x == 200!

x = 1000
if x == 1000:
    print("x == 1000!")
# x == 1000!

x = 200
if x is 200:
    print("x is 200!")
# x is 200!
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

x = 1000
if x is 1000:
    print("x is 1000!")
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

id(200)
# 140566402108616

id(1000)
# 140566385470352

id(200)
# 140566402108616

id(1000)
# 140566385470704

# ----------------------------
a = 200
b = 200

a is b
# True

a == b
# True

a = 1000
b = 1000

a is b
# False

a == b
# True

# A is B -> A == B
# A == B -> A is B <--- this is not necessarily true

# ----------------------------
1000 is 1000
# True
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

a = 1000
b = a

a is b
# True

a == b
# True

# ----------------------------
True == 1
# True

True is 1
# False
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

True == 2
# False

True is 2
# False
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

# ----------------------------
"Life" is "Life"
# True
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

str_1 = "".join(["L", "i", "f", "e"])
str_2 = "Life"

id(str_1)
# 140566385620592

id(str_2)
# 140566385620400

str_1 == str_2
# True

str_1 is str_2
# False

"Life" is ''.join(['L','i','f','e'])
# False
# <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
