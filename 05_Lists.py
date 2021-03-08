# Introduction to Lists

itemList = ['Apple', 'Banana', 'Cheese']

print(itemList)

print(itemList[0])

print(itemList[0:2])

# Add Item

itemList.append("Bread")

print(itemList)

# Add item with positioning

itemList[0] = "Supplement"

print(itemList)

# Delete Item

del itemList[2]

print(itemList)

# Get Length

print(len(itemList))

# Merge Two List

moreItem = ['Charger', 'Mobile', 'Bluetooth']

print(itemList + moreItem)

# Get Same Items Two Times

print(moreItem * 2)

# Max or Min Value in list

numList = [1, 2, 3, 4, 5]

print(max(numList))

print(min(numList))
