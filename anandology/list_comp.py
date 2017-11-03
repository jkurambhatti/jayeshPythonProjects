# Problem 24: Provide an implementation for zip function using list comprehensions.
# example
# >>> zip([1, 2, 3], ["a", "b", "c"])
# [(1, "a"), (2, "b"), (3, "c")]
#
# [(x, y) for id1,x in enumerate([1, 2, 3]) for id2,y in enumerate(["a", "b", "c"]) if id1 == id2]
#
# # Problem 25: Python provides a built-in function map that applies a function to each element of a list.
# # Provide an implementation for map using list comprehensions.
#
#
# def map(fn, l):
#     [fn(x) for x in l]
#
# map(lambda x: x * x, range(1,5))

# Problem 26: Python provides a built-in function filter(f, a) that returns items of the list a for which f(item) returns true.
# Provide an implementation for filter using list comprehensions.

# def filter(fn, l):
#     x = [a for a in l if fn(a)]
#     return x
#
# print filter(lambda x: x % 2 == 0, range(1, 10))

# Problem 28: Write a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list.

# def enumerate(l):
#     lt = [(i,x) for i,x in zip(range(len(l)),l)]
#     print lt
#
# enumerate(['a', 'b', 'c'])

# def enumerate(l):
#     lt = [(i,l[i]) for i in range(len(l)) ]
#     print lt
#
# enumerate(['a', 'b', 'c'])


# Problem 29: Write a function array to create an 2-dimensional array.
# The function should take both dimensions as arguments. Value of each element can be initialized to None:

# def array(m,n):  not working
#     k = [[].append([]).append(None) for i in range(m) for j in range(n)]
#     print k
#
# array(2,3)


# Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.

# def parse_csv(filename):
#     lines = open(filename).readlines()
#     print [line.strip().split(',') for line in lines]
#
# parse_csv('a.csv')

# Generalize the above implementation of csv parser to support any delimiter and comments.

def parse(filename, dl, c):
    lines = open(filename).readlines()
    print [line.strip().split(dl) for line in lines if not (line.strip()[0] == c)]

parse('b.csv','!', '#')
