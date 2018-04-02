num=int(input())
n=list(map(int,input().split(' ')))
for i in range(num):
    if(n[i]>n[i+1]):
        print(i+1)
        break
