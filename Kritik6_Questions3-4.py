#Question 3

#import numpy for mathematical calculations
import numpy as np

#define the density function
def normal_density(mean, variance, x):
    return 1/(np.sqrt(2*np.pi*variance**2))*np.exp(-(x-mean)**2/(2*variance**2))

#import matplotlib for plotting functions
import matplotlib.pyplot as plt

#plot the function with a mean of 10 and variance of 1
mean = 10
variance = 1
#plot on the interval whose endpoints are 4 variances away from the mean
x=np.linspace((mean - 4 * variance),(mean +  4 * variance),200)
plt.plot(x,normal_density(mean,variance,x))
plt.title("Mean = 10, Variance = 1")
plt.grid()
plt.show()

#plot the function with a mean of 5 and variance of 3
mean = 5
variance = 3
#plot on the interval whose endpoints are 4 variances away from the mean
x=np.linspace((mean - 4 * variance),(mean + 4 * variance),200)
plt.plot(x,normal_density(mean,variance,x))
plt.title("Mean = 5, Variance = 3")
plt.grid()
plt.show()

#plot the function with a mean of 2 and variance of 10
mean = 2
variance = 10
#plot on the interval whose endpoints are 4 variances away from the mean
x=np.linspace((mean - 4 * variance),(mean + 4 * variance),200)
plt.plot(x,normal_density(mean,variance,x))
plt.title("Mean = 2, Variance = 10")
plt.grid()
plt.show()

#define the approximate integral of the density function on the interval [a,b]
#use a loop to calculate the Riemann sum of the areas of 1000 rectangles whose left endpoints lie on the function
def integration(mean, variance, a, b):
    #create arrays to contain the area of each rectangle and the x-value of the left endpoint of each
    rectangle_areas = []
    rectangle_endpoints = [a]
    delta_x = (b-a)/1000
    for i in range(1,1000):
        next_area = normal_density(mean, variance, rectangle_endpoints[-1]) * delta_x
        rectangle_areas.append(next_area)
        rectangle_endpoints.append(rectangle_endpoints[-1] + delta_x)
    return sum(rectangle_areas)

#define the parameters for the density function of male's heights globally
mean = 171
variance = 7.1
#find the integral of the density function on the interval [162, 190]
#This is equal to the proportion of men with heights in this range, also the probability of a man having a height in this range
print("The probability of a man having a height between 162cm and 190cm is approximately",integration(mean, variance, 162, 190))


#Question 4

#Part a)
#define the expected value function for a uniform distribution on the interval [a,b]
#this is approximately equal to the Riemann sum of the x-values in the interval times the constant function
def E_uniform(a,b):
    function = 1/(b-a)
    x_vals = [a]
    delta_x = (b-a)/1000
    for i in range(0,1000):
        x_vals.append(x_vals[-1] + delta_x)
    return function * sum(x_vals)

#Part b)
#for an exponential distribution, E(x) equals the integral of x * λ * e^(-λx) on the interval [0,∞)
#this is approximately equal to the Riemann sum of the product of a very large number of x-values times the exponential density function for each value of x
#the parameter 'a' represents the lower limit of the interval (in this case, will be 0)
def E_exponential(a):
    #define the exponential density function, using 1/50 as λ
    def f_exponential(x):
        return (1/50)*np.exp(-1*(1/50)*x)
    #make an array of x-values to use
    x_vals = [a]
    delta_x = 1/1000
    x_times_function = []
    #multiply each x-value by the exponential density function
    for i in range(0,1000000):
        x_times_function.append(x_vals[-1] * f_exponential(x_vals[-1]) * delta_x)
        x_vals.append(x_vals[-1] + delta_x)
    #add up each x-value times its corresponding y-value (calculated using the exponential density function)
    return sum(x_times_function)
print(E_exponential(0))
#the output is 50, which makes sense because the question states that pandemics occur about every 50 years

#Part c)
#calculate the expected value of drug dosage based on height squared
#first, define the parameters for the normal density function
mean = 171
variance = 7.1
#use the same code as in part b, but replace the exponential density function with the product of the dosage function & the normal density function
#where the dosage function = 2.38 * (height ^ 2)
#& replace the interval limits with values closer to the mean (let's say within a range of 4 times the variance)
a = mean - 4*variance
b = mean + 4*variance
def E_normal(a,b):
    x_vals = [a]
    n = 10000
    delta_x = (b-a)/n
    x_times_function = []
    for i in range(0,n):
        x_times_function.append(2.38 * x_vals[-1]**2 * normal_density(mean, variance, x_vals[-1]) * delta_x)
        x_vals.append(x_vals[-1] + delta_x)
    return sum(x_times_function)
print(E_normal(a,b))