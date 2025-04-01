#choose value of x
x=1.0
#ensure x is in the interval [0,1]
if x<0.0 or x>1.0:
    print("Error!")
else:
    #find a value of n such that error is less than or equal to 0.0001
    n=1
    n_known=0
    while n_known==0:
        error=(x**(2*n+1))/(2*n+1)
        if error<=0.0001:
            n_known=1
            #calculate approximation
            a=0.0
            for i in range(0, n):
                a = a + (-1)**i*x**(2*i+1)/(2*i+1)
                i += 1
            #print outcome
            tuple=(a,n,error)
            print(tuple)
        else:
            n+=1
            