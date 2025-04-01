#import needed packages
import numpy as np
import matplotlib.pyplot as plt

#define function as f(x), learning rate as n, & initial x-value as x_0
#this part is what changes depending on the function
def f(x):
    x**2
n=0.1
x_0=1

#estimate derivative at any given point using symmetric approximation
def f_prime_approx(x):
    return (f(x+10**-10)-f(x-10**-10))/(2*10**-10)

#define linear approximation equation
def lin_approx(x):
    return -1*n*f_prime_approx(x)**2+f(x)

#create array of x-values & y-values, stating with initial values
x_vals=[x_0]
y_vals=[f(x_0)]

#set parameter i equal to 0 to track iterations of loop
i=0

#create loop that adds x & y-values until it finds x-value with derivative within 10^-10 of 0
#loop will add h to previous x-value & solve for y-value using linear approximation
while np.abs(f_prime_approx(x_vals[-1]))>10**-10:
    x_vals.append(x_vals[-1]-n*f_prime_approx(x_vals[-1]))
    y_vals.append(lin_approx(x_vals[-1]))
    i+=1
    if i>10000:
        break

#decide on what ranges of x & y-values should be plotted
plot_range=np.linspace(min(x_vals)-0.5,max(x_vals)+0.5,10000)
function_range=[f(i) for i in plot_range]

#plot function & sequence of points calculated when trying to find min
plt.plot(plot_range,function_range)
plt.plot(x_vals,y_vals)
plt.show()

#print final x & y-values (coordinates of calculated min), rounded to 3 decimals
#if statement prevents this from printing if loop hit max iterations without finding min
if np.abs(f_prime_approx(x_vals[-1]))<10**-10:
    print(round(x_vals[-1],3),round(y_vals[-1],3))