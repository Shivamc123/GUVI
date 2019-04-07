    
def alpha(x,y,z): 
    if(x>y)and(y>z):
        print(x)
    elif(y>x)and(y>z):
        print(y)
    else:
        print(z)
        
x=int(input())
y=int(input())
z=int(input())
alpha(x,y,z) 
