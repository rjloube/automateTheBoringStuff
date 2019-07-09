#! python3
# addInventory.py - this program defines a function to add items
# to the inventory of a fantasy game character.

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(v, k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return(inventory)       #w/o this, the for loop returns a value of None
            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

