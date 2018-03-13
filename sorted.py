x = input()
y = input()
z = input()
a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted : ", a1, a2, a3)
