n=input()
if(n<1 or (n%1)!=0):
    print("wrong input")
else:
    temp=0
    while(n!=0):
        temp=temp+n
        n=n-1
    print (temp)
