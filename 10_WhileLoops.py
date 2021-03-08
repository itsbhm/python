# While Loops

x = 0

while x < 5:
    print(x)
    x = x + 1

# ----
y = 0

while y < 5:
    print(y)
    if y == 2:
        break
    y = y + 1

# ----
z = 0

while z < 7:
    z = z + 1
    if z == 3:
        continue
    print(z)

# ----
xyz = 0

while xyz < 7:
    xyz = xyz + 1
    if xyz == 3:
        pass
    print(xyz)
