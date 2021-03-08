# For Loops

listF = ['Apple', 'Orange', 'Papaya']

for item in listF:
    print(item)

# ----
tupL = (10, 11, 18)

for val in tupL:
    print(val)

# ----
for i in range(0, 5):
    print(i)

for i in range(1, 6):
    print(i)

# Adding 2 in each output value
for i in range(0, 11, 2):
    print(i)

# Nested for loop
for i in range(0, 5):
    for j in range(0, 3):
        print(1*j)
