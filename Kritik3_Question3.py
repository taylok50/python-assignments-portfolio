import numpy as np

def f(x): #these values can be switched out for others
    return x**2
    #also works for f(x)=x**2 or f(x)=np.sin(x)
c=1
#try c=1 for f(x)=x**2 or c=np.pi/4 for f(x)=np.sin(x)
E=0.1
#try E=0.1 for f(x)=x**2 or E=0.01 for f(x)=np.sin(x)

def f_prime(x): #derivative using central difference
        return (f(x+10**-8)-f(x-10**-8))/(2*10**-8)
def L(x): #linear approximation
    return f(c)+f_prime(c)*(x-c)

for i in range (10**10): #find x1
    x1=c-10**-5*(i+1) #use x values moving AWAY from c
    if np.abs(f(x1)-L(x1))>E:
    #finds first x value outside of error range (error > E)
        print("x1=",x1)
        break
else:
    print("No x1 value found")

for i in range (10**10): #find x2 in the same way
    x2=c+10**-5*(i+1)
    if np.abs(f(x2)-L(x2))>E:
        print("x2=",x2)
        break
else:
    print("No x2 value found")

