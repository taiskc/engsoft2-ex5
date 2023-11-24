def is_valid_numeric_input(a, b):
    return (type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)

def add(a, b):
    if not is_valid_numeric_input:
        return "Only number allowed!"
    return a + b

def subtract(a, b):
    if not is_valid_numeric_input:
        return "Only number allowed!"    
    return a - b

def multiply(a, b):
    if not is_valid_numeric_input:
        return "Only number allowed!"
    return a * b

def divide(a, b):
    if not is_valid_numeric_input:
        return "Only number allowed!"
    if b == 0:
        return "Cannot divide by zero!"
    return a / b