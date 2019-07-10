from collections import Counter
x=int(input())
n = input().split()
y=Counter(n)
print(min(y,key=y.get))
