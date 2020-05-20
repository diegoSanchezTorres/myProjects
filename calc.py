#functions
def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError('You cannot divide by 0')
    return a/b
def power(a,b):
    return a**b
def module(a,b):
    return a%b
def intdivision(a,b):
    if b==0:
        raise ValueError('You cannot divide by 0')
    return a//b

#Main
print(addition(5,10))
print(subtract(5,10))
print(multiply(5,10))
print(divide(5,1))
print(power(5,10))
print(module(5,10))
print(intdivision(5,1))
