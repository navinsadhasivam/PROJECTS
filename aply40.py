num=int(input())
n=0
for x in range(num+1):
	for y in range(num+1):
		way=(x*1)+(y*2)
		if way==num:
			n+=1
print(n)
