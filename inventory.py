#! python3
# inventory.py - this program displays the inventory from a dictionary
# for a fantasy game character.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(v, k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
