# Introduction to Dictionaries (Key and Value)

listX = ["A", 12, "B", 14, "C", 20]

print(listX)

students = {
    "A": 12,
    "B": 14,
    "C": 20
}

print(students["A"])

# Set a New Value (Update)

students["B"] = 20

print(students)

# Delete a Value (Delete)

del students["C"]

print(students)

# Get Length

print(len(students))

# Duplicate Keys

listY = {
    "A": 12,
    "A": 14,
    "A": 20
}

# Note: You will get the last matched key value

print(listY["A"])
