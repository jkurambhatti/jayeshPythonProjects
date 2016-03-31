import os
import sys
''' this is used for
    multiline commnts
'''

# this is used for single line comment

print('hello my viewers')
print ("i have somethin for ya")

firstname = 'jayesh'
secondName = 'k'

print (firstname + " " + secondName)
firstname += secondName    # this is how we concatanate strings

# another way to concatenate

firstname.capitalize()
print len(firstname)   #find len of string

print firstname[:3]  # prints first 3 char but index 3 is not included so 0,1,2 op: jay
print firstname[3:]  # prints all chars after 3 char but index 3 is included  op: eshk
print firstname[:]  # prints entire string
print firstname[-3]  # prints last 3rd char in reverse operation it begins with -1 since -0 is 0
print firstname[-0]  # since -0 = 0 hence first character
print firstname[:-3]  # prints all chars except from last 3 "jaye"
print firstname[2:-2]  # prints all chars from 2nd index to last second index "yes"





