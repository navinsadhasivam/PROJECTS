l=list(input())
m=[]
for x in l:
    if x.isdigit():
        m.append(x)
print("".join(str(n) for n in m))
