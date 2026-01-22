grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

price_of_eggs = grocery_inventory["Eggs"][1]
if price_of_eggs > 5.00:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = ("Dairy", price_of_eggs - 1, 30)
        
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

stock_of_milk = grocery_inventory["Milk"][2]
if stock_of_milk < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = ("Dairy", 3.50, stock_of_milk + 20)
    
else:
    print("Milk has sufficient stock.")
    
price_of_apples = grocery_inventory["Apples"][1]
if price_of_apples > 2.00:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)