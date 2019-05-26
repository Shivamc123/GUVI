def firstNonRepeating(a, n): 
  
    for i in range(n): 
        j = 0
        while(j < n): 
            if (i != j and a[i] == a[j]): 
                break
            j += 1
        if (j == n): 
            return a[i] 
      
    return -1
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(b[i])
print(firstNonRepeating(a, n))
