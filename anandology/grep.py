# Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

import sys

def grep():
    string = sys.argv[1]
    filename = sys.argv[2]
    for line in open(filename).readlines():
        if string in line:
            print line.strip()

grep()
