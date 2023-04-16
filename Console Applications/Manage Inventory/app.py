Inventory = []

def ApplicationGreeting():
    print("Inventory Item Application \n")

def AddItems(Inventory):
    numberItems = int(input("How many items would you like to add?") )

    i = 0
    while i < numberItems:
        item = input("Enter item: ").lower().strip()
        Inventory.append(item)
        i += 1

def InquireInventory(Inventory):
    print("Current items in inventory: ")
    for x in Inventory:
        print(x)

def RemoveItem(Inventory):
    itemRemove = input("What item would you like to remove: ").lower().strip()
    if itemRemove in Inventory:
        Inventory.remove(itemRemove)
    else:
        print(f"The item " + itemRemove + " does not exist in the inventory.")

# To do: 
# Continuously run until forced to stop
# Close program
# Save report