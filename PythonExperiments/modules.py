'''
    this teaches you how to create your own module
    use : suppose there are a no. of functions which are used in most of files
     so you wouid not write them in every single file
     you can simply club all these commonly used functions and import the module in whicheer file reqd
'''


import calculator
import random

calculator.add(10,20,30,50)
calculator.div(100,20)
calculator.mul(10,2,3,5)

i = random.randrange(0, 10)     # random is also a module written by a deveolper
print i