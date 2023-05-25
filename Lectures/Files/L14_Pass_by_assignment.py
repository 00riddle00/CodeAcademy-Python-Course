# ----------------------------
a = 1
b = 2

id(a)
# 139755945128936

id(b)
# 139755945128968

b = 1 + 1
id(b)
# 139755945128968

a = 3
b = 3
id(a)
id(b)

a = 1000
b = 1001

id(a)
# 139755945129000

id(b)
# 139755945129000

# ----------------------------
a = 800
id(a)
# 139755929512432

b = a
id(b)
# 139755929512432

a = 1000
id(a)
# 139755929509744

b = a - 200
print(b)
# 800

id(b)
# 139755929512848

# ----------------------------
a = 1
b = 2

id(a)
# 139755945128936

id(b)
# 139755945128968

# Pass by assignment
def fun_1(a, b):
    print(id(a))
    print(id(b))
    print()
    a = 10
    b = 20
    print(id(a))
    print(id(b))

fun_1(a,b)
# 139755945128936
# 139755945128968

# 139755945129224
# 139755945129544

# ----------------------------
a = 2
b = 3

id(a)
# 139755945128968

id(b)
# 139755945129000

# Pass by assignment
def fun_2(a, b):
    print(id(a))
    print(id(b))
    print()
    a = a + 10
    b = b + 20
    print(id(a))
    print(id(b))

fun_2(a,b)
# 139755945128968
# 139755945129000

# 139755945129288
# 139755945129640

# Pass by assignment - behaves like pass by value,
# except that if we do not perform any assignment,
# the same object is reused, which was passed to
# the function.

# ----------------------------
# Pass by value (Pascal) (function/procedure head)
procedure pass_by_value(a: integer);

# Pass by reference (Pascal) (function/procedure head)
procedure pass_by_reference(var a: integer);
