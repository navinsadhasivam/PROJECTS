m=int(input())
n=[]
for x in range(0,m):
    p=input()
    n.append(p)
q=[]
for x in n:
    if x not in q:
        q.append(x)
q.sort(reverse=True)
print ("".join(q))
