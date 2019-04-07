    
def alpha(x,y,z): 
    if(x>y)and(y>z):
        print(x)
    elif(y>x)and(y>z):
        print(y)
    else:
        print(z)
        
x,y,z= [int(x) for x in input("").split()]
alpha(x,y,z)
