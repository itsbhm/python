#Placeholders in Strings

name = "Mini"
fullStr1 = " is 21 years old"

print(name + fullStr1)

# ------
fullStr2 = "%s is 21 years old"

print(fullStr2 % ("Eva"))

# ------
newName = "Samantha"

print(fullStr2 % newName)

# ------
fullStr3 = "Today the day is %s and the year is %s"

day = "Tue"
year = 2021

print(fullStr3 % (day, year))

# ------
fullStr4 = "%s is %d year old now!"

print(fullStr4 % (name, 24))
