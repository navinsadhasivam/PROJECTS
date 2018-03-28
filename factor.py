s=int(input())
l=[]
for i in range(1, s + 1):
       if s % i == 0:
           l.append(i)
print(" ".join(str(n) for n in l))
