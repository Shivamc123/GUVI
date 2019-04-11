import collections

n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(b[i])

results = collections.Counter(a)
c = []
for i in results:
	if(results[i]==1):
		c.append(i)
print(" ".join(c))
