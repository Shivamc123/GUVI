from collections import Counter
x=int(input())
l = input().split()
y=Counter(l)
print(min(y,key=y.get))
