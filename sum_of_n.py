
    
def check():
    try: 
        n=int(input())
        a=(n*(n+1))/2
        print(int(a))
    except ValueError:
            print("invalid")
check()
        
