def maxSubArraySum(a,size): 
      
    max_so_far =a[0] 
    curr_max = a[0] 
      
    for i in range(1,size): 
        curr_max = max(a[i], curr_max + a[i]) 
        max_so_far = max(max_so_far,curr_max) 
          
    return max_so_far 
n=int(input())
a=[]
x=[int(x) for x in input().split()]
for i in range (0,n):
  a.append(x[i])
print(maxSubArraySum(a,len(a)))
