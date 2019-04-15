def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        print("YES") 
    else: 
        print("NO")  
           
n,m =[int(x) for x in input().split()]
a = []
b = input().split()
for i in range(0,n):
	a.append(b[i])
c=[]
d=input().split()
for i in range(0,m):
	c.append(d[i])
common_member(a,c) 
   
