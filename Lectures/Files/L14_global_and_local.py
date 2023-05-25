# ----------------------------
global_var = 1

def fun_1():
    local_var = 2
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

fun_1()
# 3

other_sum = global_var + local_var
# NameError: name 'local_var' is not defined.

# ----------------------------
global_var = 1

def fun_2():
    local_var = 2
    global_var = 3
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

fun_2()
# 5

other_sum = global_var + local_var
# NameError: name 'local_var' is not defined.

# ----------------------------
global_var = 1

def fun_3():
    local_var = 2
    global_var = global_var + 2
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

fun_3()
# UnboundLocalError: cannot access local variable 'global_var' where it is not associated with a value

other_sum = global_var + local_var
# NameError: name 'local_var' is not defined.

# ----------------------------
global_var = 1

def fun_4():
    global global_var
    local_var = 2
    global_var = global_var + 2
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

fun_4()
# 5

other_sum = global_var + local_var
# NameError: name 'local_var' is not defined.

# ----------------------------
global_var = 1

def fun_5():
    global local_var
    local_var = 2
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

other_sum = global_var + local_var
# NameError: name 'local_var' is not defined.

fun_5()
# 3

other_sum = global_var + local_var
other_sum
# 3

# ----------------------------
global_var = 1

def fun_6():
    local_var = 2
    _sum = global_var + local_var
    print(_sum)
    global local_var
    # SyntaxError: name 'local_var' is used prior to global declaration

# ----------------------------
global_var = 1

def fun_7():
    local_var = 2
    global_var = 3
    _sum = global_var + local_var
    print(_sum)

global_var
# 1

fun_7()
# 5

global_var
# 1

