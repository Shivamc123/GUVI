n=int(input())
a=[]
x=[int(x) for x in input().split()]
for i in range (0,n):
  a.append(x[i])
a.sort()
print(int(a[0]))
