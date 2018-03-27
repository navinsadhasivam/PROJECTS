s=int(input())
if s == 0:
    print(1)
if s & (s - 1) == 0:
    print(s)
while s & (s - 1) > 0:
    s &= (s - 1)
print(s << 1)
