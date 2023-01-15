oliver_bag = {"Laptop", "Notebook", "Pen", "Sunglasses", "Hand sanitizer"}
ethan_bag = {"Sunglasses", "Notebook", "Phone"}
mia_bag = {"Laptop", "Sunglasses", "Hand sanitizer"}

# What are the common items in Oliver's and Ethan's bag?
common_items = oliver_bag.intersection(ethan_bag)
print("The common items in Oliver's and Ethan's bag are:", common_items)

# What are the items that in Oliver's bag but not in Mia's bag?
items_in_oliver_not_in_mia = oliver_bag.difference(mia_bag)
print("The items that are in Oliver's bag but not in Mia's bag are:", items_in_oliver_not_in_mia)

# What are the common items in Oliver's, Ethan's and Mia's bag?
common_items_in_all_bags = oliver_bag.intersection(ethan_bag, mia_bag)
print("The common items in Oliver's, Ethan's and Mia's bag are:", common_items_in_all_bags)
