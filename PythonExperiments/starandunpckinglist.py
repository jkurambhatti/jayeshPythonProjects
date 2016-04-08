'''
    write a function which will take a list of integers,
    drop 1st and last element
    and print average of middle elements
'''

l1 = [10,2,3,4,5,6,7,8,9]

def average_middle(marks):
    #first, *middle, last = marks
    print "average : " , sum(marks) / len(marks)


average_middle(l1)

'''
    unpacking lists: if you want to categorise the list directly at the time of initialization here's the way

'''

books = ['da vinci code', 'dan brown', 125.50]
# its a long way to copy that's why we use unpacking of lists
name = books[0]
author = books[1]
price = books[2]

for i in books:
    print i


name, author, price = ['da vinci code', 'dan brown', 125.50]
print name
print author
print price