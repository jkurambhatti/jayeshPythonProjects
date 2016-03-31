''' sets are similar to lists except in { } , lists contain [ ]
   values cannot be repeated in sets, every value is unique
   values can be repeated in lists
'''


groceries = { 'milk', 'atta', 'rice', 'dal', 'sugar', 'salt', 'atta' }

#as you can notice 'atta' is repeated in groceries

print groceries

# o/p : set(['dal', 'sugar', 'atta', 'rice', 'salt', 'milk'])
# atta is seen only once , hence every value in a set is unique

#this is how you look for elemetn in sets

if 'dal' in groceries:
    print "yes , no need to write again"
else:
    print "nope not present in list"
