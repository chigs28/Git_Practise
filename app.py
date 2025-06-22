def addition(a, b, c):
    """Returns the sum of a and b."""
    return a + b + c

def subtraction(a, b, e):
    """Returns the difference of a and b."""
    return a - b - e

def division(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
