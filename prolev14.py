xjj,xkk=map(int,input().split())
list1=list(map(int,input().split()))
xjj=[]
list1.insert(0,0)
for y in range(xkk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=list1[i]     
     xjj.append(sumup)
for y in xjj:
    print(y)
