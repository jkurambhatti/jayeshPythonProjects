# Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.

import sys

# def head():
#     filename = sys.argv[1]
#     for line in open(filename).readlines()[:10]:
#         print line.strip()


# head()

def tail():
    filename = sys.argv[1]
    for line in open(filename).readlines()[-10:]:
        print line.strip()

tail()
