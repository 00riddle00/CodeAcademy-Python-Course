def A_and_B(A, B):
    is_whole_statement_true = False

    if A is True:
        if B is True:
            is_whole_statement_true = True
        elif B is False:
            is_whole_statement_true = False
    elif A is False:
        is_whole_statement_true = False
        # ...
        # There was no need to check if B is True here
        # ---At this step we save the time of checking B---

    return is_whole_statement_true

print( A_and_B(False, False) ) # A = False, B = False
print( A_and_B(False, True ) ) # A = False, B = True
print( A_and_B(True,  False) ) # A = True,  B = False
print( A_and_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------

# a simplified version (same logic)
def A_and_B(A, B):
    if A:
        if B:
            return True
        else:
            return False
    else:
        return False

print( A_and_B(False, False) ) # A = False, B = False
print( A_and_B(False, True ) ) # A = False, B = True
print( A_and_B(True,  False) ) # A = True,  B = False
print( A_and_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
# ----------------------------------------------------------

# a completely simplified version
def A_and_B(A, B):
    return A and B

print( A_and_B(False, False) ) # A = False, B = False
print( A_and_B(False, True ) ) # A = False, B = True
print( A_and_B(True,  False) ) # A = True,  B = False
print( A_and_B(True,  True ) ) # A = True,  B = True
print(10 * '-')
