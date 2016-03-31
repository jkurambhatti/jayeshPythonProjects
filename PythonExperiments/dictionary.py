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
    print k , v

    