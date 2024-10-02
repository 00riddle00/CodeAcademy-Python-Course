# The order of function arguments, at least my interpretation of it:

# 1 (one): Positional arguments, required.
# 2 (two): A forward-slash (/) says that all arguments to the left of it are positional-only.
# 3 (three): Positional arguments with default values, optional.
# 4 (four): *args - any additional positional arguments which must be passed without a keyword. If
#           only a '*' is used, then all arguments to the right of it are keyword-only.
# 5 (five): Keyword-only arguments, required.
# 6 (six): Keyword-only arguments with default values, optional.
# 7 (seven): **kwargs - any additional keyword arguments which must be passed with a keyword.

def fun(one, /, three=3, *args, five, six=6, **kwargs):
    print("one:", one)
    print("three:", three)
    if args:
        print("args:", args)
    print("five:", five)
    print("six:", six)
    if kwargs:
        print("kwargs:", kwargs)
    print("------")

# Legal function calls:
fun(1, five=5)
fun(1, 3, five=5)
fun(1, three=3, five=5)

fun(1, five=5)
fun(1, five=5, six=6)
fun(1, 3, five=5, six=6)
fun(1, three=3, five=5, six=6)

fun(1, five=5)
fun(1, 4, five=5)
fun(1, 3, 4, five=5)
fun(1, 3, 4, five=5, six=6)

fun(1, five=5)
fun(1, five=5, seven=7)
fun(1, 3, five=5, seven=7)
fun(1, three=3, five=5, seven=7)
fun(1, five=5, six=6, seven=7)
fun(1, 3, five=5, six=6, seven=7)
fun(1, three=3, five=5, six=6, seven=7)
fun(1, 4, five=5, seven=7)
fun(1, 3, 4, five=5, seven=7)
fun(1, 3, 4, five=5, six=6, seven=7)
