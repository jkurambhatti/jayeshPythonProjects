# Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width

import sys

def wrap():
    filename = sys.argv[1]
    wraplen = int(sys.argv[2])
    print filename, wraplen
    wrappedLines = []
    for line in open(filename).readlines():
        line = line.strip()
        if len(line) > wraplen:
            [wrappedLines.append(line[i:i+wraplen]) for i in range(0, len(line), wraplen)]
        else:
            wrappedLines.append(line)

    for wline in wrappedLines:
        print wline

wrap()
