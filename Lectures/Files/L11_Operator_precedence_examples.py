# ref: https://docs.python.org/3/reference/expressions.html#operator-precedence

res1 = 1 == 1 or 2 == 2
# ^--evaluates to:
res1 = True or 2 == 2
# ^--evaluates to:
res1 = True or True
# ^--evaluates to:
res1 = True

res2 = not 2 * 2 == 4
# ^--evaluates to:
res2 = not 4 == 4
# ^--evaluates to:
res2 = not True
# ^--evaluates to:
res2 = False
