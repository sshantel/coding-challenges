"""
Write a recursive python function that receives 2 integer parameters and 
returns the first parameter raised to the power of the 2nd parameter. 
Ask the user to enter 2 integers greater than 0. 

>>> power(2,3)
8
>>> power(3,2)
9
>>> power(1,0)
1
"""

N, P = input("Enter 2 Integers greater than 0: ").split(',')
def power(N, P): 
    # if power is 0 or 1 then number is returned
    if (P == 0):
        return 1
    elif (P == 1):
        return int(N)
    else:
        return (int(N) * power(int(N), int(P)-1))
# Driver program 
print(power(N, P))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED.\n")