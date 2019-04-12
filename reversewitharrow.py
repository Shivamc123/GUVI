
n=int(input())
a=[]
x=[int(x) for x in input().split()]
for i in range (0,n):
  a.append(x[i])
print(*a[::-1], sep="->")
