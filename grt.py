n = sorted(map(int,raw_input().split(" ")))
print max([i for i in range(1,n[1]+1) if (n[0]%i==0) and (n[1]%i==0)])
