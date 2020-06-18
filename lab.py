l=[int(x) for x in input().split(",")]
a=[]
for i in range(0,len(l)):
	if(l[i]%3==0):
		a.append("T")
	elif(l[i]%5==0):
		a.append("F")
	elif(l[i]%3==0 and l[i]%5==0):
		a.append("TF")
	else:
		a.append("O")
print(", ".join(a))
