import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def square_root(a):
    return math.sqrt(a)
def cube_root(a):
    return a ** (1/3)
def power(a, b):
    return a ** b
def cube(a):
    return a ** 3
