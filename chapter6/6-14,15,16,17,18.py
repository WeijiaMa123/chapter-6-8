import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def is_odd(n):
    if n%2 == 1:
        return True
    else:
        return False


def is_factor(f,n):
    if f <n or f == n:
        if n%f==0:
            return True
        else:
            return False
    else:
        return False
    
    


def test_suite():
    test(is_even(3)==False)
    test(is_even(0)==True)
    test(is_odd(1234565434567897678)==False)
    test(is_odd(973428797987234993)==True)
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))


test_suite()