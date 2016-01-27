#  Dmitriy Gutnik 77099786 and Derek Tran 30992349. ICS Lab 12. Lab Asst 1D.
def factorial (n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)
assert factorial (0) == 1
assert factorial (5) == 120

print("120! is", factorial(120))
print("50*10! is", factorial(50*10))
print("(5!)! is", factorial(factorial(5)))
