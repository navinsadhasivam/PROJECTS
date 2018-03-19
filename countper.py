l=int(input("Intial number:"))
r=int(input("final value:"))
for x in range(l+1,r):
	for y in range(1,r):
		temp=y*y
		if temp==x:
			print(x)
