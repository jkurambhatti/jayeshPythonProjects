# def cumsum(l):
#     for index, value in enumerate(l):
#         if index == 0:
#             l[index] = value
#         else:
#             l[index] = sum(l[index - 1: index + 1])
#
#     print l
#
# cumsum(range(1,5))
#
#
# def product(l):
#     k = 1;
#     for x in l:
#         k = k * x
#
#     return k
#
# def cumprod(l):
#     for index, value in enumerate(l):
#         if index == 0:
#             l[index] = value
#         else:
#             l[index] = product(l[index - 1: index + 1])
#
#     print l
#
# cumprod(range(1,5))

# def unq_list(l):
#     x = []
#     for k in l:
#         if not (k in x):
#             x.append(k)
#
#     print x
#
# unq_list([1,2,3,1,2,3])


# def group(l, size):
#     gl = []
#     for x in range(len(l))[::size]:
#         gl.append(l[x:x + size])
#
#     print gl
#
# group(range(1,11),3)

# Write a function extsort to sort a list of files based on extension.

def extsort(l):
    l.sort(key=lambda x: x.split('.')[-1])
    print l


print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
