n,m=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
s=[]
for x in l:
    if(x%2!=0):
        s.append(x)
print(s[m-1])
