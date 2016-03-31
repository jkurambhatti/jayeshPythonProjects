def add(*args):
    result = 0
    for i in args:
        result = result + i
    print result

def sub(*args):
    result = 0
    for i in args:
        result =  i - result
    print result


def mul(*args):
    result = 1
    for i in args:
        result = result * i
    print result

def div( n, d ):
    result = n / d
    print result


def power (a, b):
    print a ** b
