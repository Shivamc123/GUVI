    
def check():
    try: 
        a=int(input())
        if(a%4==0):
            print("yes")
        else:
            print("no")
    except ValueError:
            print("invalid")
check()
        
