# Lists of items and categories for slicing
           # 01234567890123456789012345678
items = "Bubblegum, Chocolate, Pasta"  #27
categories ="Candy Aisle, Pasta Aisle"  #24

candy1 = items[0:9]                #bubblegum
candy2 = items[11:20]               #chocolate
dry_goods = items[22:27]            #pasta
 
category1 = categories[0:11]       #Candy aisle
category2 = categories[13:24]        #pasta asile

bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")