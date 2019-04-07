def check():
    try: 
        x, y = [int(x) for x in input("Enter two value: ").split()]
        a=[]
        sum=0
        for i in range(1,x+1):
            a.append(i)
        for j in range(0,y):
            sum=sum+a[j]
        print(sum)
    except ValueError:
           print("invalid")
check()
        
