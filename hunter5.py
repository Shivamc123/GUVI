st=list(map(str,input()))
v=t=0
for i in range(0,len(st)-1):
  q=st[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+st[j]
    if int(q)<27 and int(q)>0: v=v+1
    elif int(q)==0: v=v-1
    else: break
if v!=1: t=v%2
print(v+t+1)
#shivam@
