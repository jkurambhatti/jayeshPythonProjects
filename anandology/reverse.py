# # Problem 17: Write a program reverse.py to print lines of a file in reverse order
# # example
#
# $ cat she.txt
# She sells seashells on the seashore;
# The shells that she sells are seashells I'm sure.
# So if she sells seashells on the seashore,
# I'm sure that the shells are seashore shells.
#
# $ python reverse.py she.txt
# I'm sure that the shells are seashore shells.
# So if she sells seashells on the seashore,
# The shells that she sells are seashells I'm sure.
# She sells seashells on the seashore;

import sys

# def reverse():
#     filename = sys.argv[1]
#     lines = open(filename).read().split('\n')
#     linesInReverse = lines[::-1]
#     for line in linesInReverse:
#         print line
#
# reverse()

# Problem 18: Write a program to print each line of a file in reverse order.

def reverseLine(line):
    words = line.split()
    return ' '.join(words[::-1])

def reverseEveryLine():
    filename = sys.argv[1]
    lines = open(filename).readlines()
    reverseLines = []
    for line in lines:
        reverseLines.append(reverseLine(line));

    print reverseLines


reverseEveryLine()
