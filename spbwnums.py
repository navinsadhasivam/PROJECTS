n=raw_input()
length=len(n)
for i in range(0,length):
	if(n[i]=="k"):
		print n[i]
		break
	elif(n[i]=="K"):
		print n[i]
		break
	else:
		print n[i],
