'''
    zip command is used to zip 2 lists, some what like dictionary
    what we will do is
    take 2 list of sorted integers
    zip them and create a new list which is union of 2 lists
    this is also a sorted list

'''


list1 = [0,2,8,6,4]
list2 = [1,3,9,7,5]

list1.sort()
list2.sort()

print list1
print list2

list3 = zip(list1, list2)
list4 = []

for a, b in list3:
    if a < b:
        list4.append(a)
        list4.append(b)
    else:
        list4.append(b)
        list4.append(a)

print list4


