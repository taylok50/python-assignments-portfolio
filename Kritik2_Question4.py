import numpy as np #numpy is needed so we can use mathematical constants
np.seterr(divide='ignore') #this prevents an error message from appearing if the function includes division by 0

#we must input a and b (the endpoints of our interval) as well as f (the function)
#this code uses the first test case as an example, but a, b, & f could be changed
a=0
b=1
n=3
#we can create a table of values of x with the 2 endpoints and the midpoint
x=np.linspace(a,b,n)
f=np.exp(x)+np.log(x)

i=0
for i in range(0,n):
    if f[i-1] * f[i] < 0:
    #this checks to see if the sign of f(x) changes between the tested values
        if np.abs(x[i] - x[i - 1]) < 10**-10:
            # this only applies when the first 10 decimal places of the interval endpoints are equal
            # it indicates that we found a solution that is correct to 10 decimal places
            print("One solution of f(x)=0 on the given interval is ", "%.10f" %x[i])
            #"%.10f" tells Python to print 10 decimal places
            break
        else:
            a=[i-1]
            b=[i]
            i=0
            #this redefines a and b so that our interval is now smaller and the loop will repeat
            #i=0 forces the loop to start from the lower end of the interval again