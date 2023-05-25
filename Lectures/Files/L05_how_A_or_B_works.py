def A_or_B(A, B):
    is_whole_statement_true = False

    if A is True:
        is_whole_statement_true = True
        # ...
        # There was no need to check if B is True here
        # ---At this step we save the time of checking B---
    elif A is False:
        if B is True:
            is_whole_statement_true = True
        elif B is False:
            is_whole_statement_true = False

    return is_whole_statement_true

print( A_or_B(False, False) ) # A = False, B = False
print( A_or_B(False, True ) ) # A = False, B = True
print( A_or_B(True,  False) ) # A = True,  B = False
print( A_or_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------

# a simplified version (same logic)
def A_or_B(A, B):
    if A:
        return True
    else:
        if B:
            return True
        else:
            return False

print( A_or_B(False, False) ) # A = False, B = False
print( A_or_B(False, True ) ) # A = False, B = True
print( A_or_B(True,  False) ) # A = True,  B = False
print( A_or_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------

# a completely simplified version
def A_or_B(A, B):
    return A or B

print( A_or_B(False, False) ) # A = False, B = False
print( A_or_B(False, True ) ) # A = False, B = True
print( A_or_B(True,  False) ) # A = True,  B = False
print( A_or_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------
