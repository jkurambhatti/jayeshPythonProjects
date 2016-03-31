import os
import sys
'''
shows you how to use for loop
also shows how to use range()
also wew will learn about while loop

the catch oint is indentation
indentation is how interpreter interprets the part of loop
'''


grocery = ['oil', 'rice', 'aatta', 'sugar', 'spices']

print grocery # prints all items in the grocery variable
'''
for i in grocery:       # i here is called placeholder so it basically points to every item in the list and is increm
                        # incremented automatically
    print i             # it means for each item item in grocery
    #print len(i)
'''

''' suppose you want value of first 3 items in grocery
'''

# this one works fine
'''
for f in grocery[:3]:
    print(f)
'''
# this one does not work due indentation
# error : IndentationError: unexpected indent

for f in grocery[:3]:
    print (f)

# so make sure indentation is correct


# how to use range()

#for i in range(10):   # 0 - 9 sincew last digit not included
# if you forget ':' , then error - SyntaxError: invalid syntax

#for i in range(4, 12):   # prints from 4 to 11 (since last value not included)

for i in range(10,50,5):    # prints 10 to 50 with step of 5 10 15 20 25 30 35 40 45
    print i

'''
thus it means that the range() is overloaded for different number of arguments it receives
'''
x = 10

# simple implementation of while loop
while x <= 15:
    print x
    x += 1

