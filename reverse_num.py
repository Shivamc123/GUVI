
    
def check():
    try: 
       x=int(input())
       rev=0
       while(x!=0):
           d=x%10
           rev=rev*10+d
           x=x//10
       print(rev)
    except ValueError:
           print("invalid")
check()
        
