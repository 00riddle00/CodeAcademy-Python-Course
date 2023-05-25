# Logical OR
# (There is also a bitwise OR, |)
def A_or_B(A, B):
    return A or B

print( A_or_B(False, False) ) # A = False, B = False
print( A_or_B(False, True ) ) # A = False, B = True
print( A_or_B(True,  False) ) # A = True,  B = False
print( A_or_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------

# Logical XOR
# (There is also a bitwise XOR, ^)
def A_xor_B(A, B):
    return A != B
    # we can also write:
    # return A is not B

print( A_xor_B(False, False) ) # A = False, B = False
print( A_xor_B(False, True ) ) # A = False, B = True
print( A_xor_B(True,  False) ) # A = True,  B = False
print( A_xor_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------
