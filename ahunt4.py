a=int(input())
b=[]
for x in range(0,a):
    c=input()
    b.append(c)
for i in b:
  count=b.count(i)
  if count==1:
    print(i)
