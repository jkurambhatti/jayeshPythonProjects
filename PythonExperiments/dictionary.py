# DICTIONARY is similar to maps
# it has key-value pairs


menu_card = { "panner butter masala" : 200,
              "mushroom masala" : 250,
              "kaju curry" : 180,
              "veg kolhapuri" : 150,
              "dal tadka" : 120,
              "lassi" : 50
              }

print menu_card     # prints all k - v pairs

print menu_card['lassi']    # 50

for k, v in menu_card.items():  # another way to access key value pairs
    print k, v


# to find the min, max and sort the dictionary items

print menu_card.values()    # print all values from key:value pair
print  menu_card.keys()     # print all keys from key:value pair

print min(menu_card.values())   # 50
print max(menu_card.values())   # 250

print sorted(menu_card.values())    # print all sorted values from key:value pair

# a function called zip() is used to zip 2 lists together
# the only thing to remember is that what ever list you pass first only that shall be acted upon
# so if u want to sort accord. to values then zip values list first : eg :



menu_card_zipped = zip(menu_card.values(), menu_card.keys())
print min(menu_card_zipped) # prints the value and key associated together
# output : (50, 'lassi')

print max(menu_card_zipped)
#ouptput : (250, 'mushroom masala')

print sorted(menu_card_zipped)
# output : (50, 'lassi'), (120, 'dal tadka'), (150, 'veg kolhapuri'), (180, 'kaju curry'), (200, 'panner butter masala'), (250, 'mushroom masala')]

