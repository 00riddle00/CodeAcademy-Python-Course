# ----------------------------
expression = "print(15)"
expression
# 'print(15)'

type(expression)
# <class 'str'>

eval(expression)
# 15

eval("5 + 2")
# 7

# ----------------------------
code = compile("print(55)", "test", "eval")
code
# <code object <module> at 0x7fdb8a91f5d0, file "test", line 1>

type(code)
# <class 'code'>

exec(code)
# 55

# ----------------------------
code_block = """
def add_10(a):
    return a + 10

print(100 + add_10(20))
"""

print(code_block)

compiled_code_block = compile(code_block, "test", "exec")

exec(compiled_code_block)
# 130
