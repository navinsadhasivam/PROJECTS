p=int(input())
q=[]
for x in range(0,p):
    r=input()
    q.append(r)
s=[]
t=[]
for x in q:
    if x not in s:
        s.append(x)
    else:
        t.append(x)
t.sort()
u=[]
for x in t:
    if x not in u:
        u.append(x)
print (u)
