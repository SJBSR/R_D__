# Inventory management

inv = ["Sword", "Shield", "Health Potion"]

if all(inv):
    print("Inventory is full.")
elif any(inv):
    print("Inventory has some items.")
else: 
    print("Inventory is empty.")