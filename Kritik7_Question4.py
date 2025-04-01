#import needed packages
import numpy as np
from scipy.special import gamma

#define the probability density function of the t-distribution at point x with nu degrees of freedom
def t_distribution_pdf(x, nu):
    coeff = gamma((nu+1)/2)/(np.sqrt(nu*np.pi)*gamma(nu/2))
    density = coeff*(1+x**2/nu)**(-0.5*(nu+1))
    return density

#make an array with the test score data
scores = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]

#define the national average
mu_0 = 75

#define functions to calculate the mean & standard deviation of a set of data
def mean(x):
    return sum(x)/len(x)
def st_dev(x,avg):
    square = []
    for i in range(0,len(x)):
        square.append((x[i]-avg)**2)
    total = sum(square)
    return np.sqrt((1/(len(x)-1))*total)

#print the mean & standard deviation of the test scores
print("The mean test score is ", mean(scores),".")
print("The standard deviation of the test scores is ", st_dev(scores,mean(scores)),".")

#write a function for t_0
def t_0(x_bar,mu,st_dev,x):
    return (x_bar-mu)/(st_dev/np.sqrt(len(x)))

#print t_0
print("t_0 =",t_0(mean(scores),mu_0,st_dev(scores,mean(scores)),scores))

#now a function to calculate t_*
def find_t_star(prob,nu,x_start=0,x_end=20,num_points=10000):
    x = np.linspace(x_start,x_end,num_points)
    y = t_distribution_pdf(x,nu)
    cdf = np.cumsum(y)*(x[1]-x[0])
    target_half_prob = prob/2
    index = np.where(cdf>=target_half_prob)[0][0]
    return x[index]

#print t_* for the test scores with certainty 0.95
print("t_star = ",find_t_star(0.95,(len(scores)-1)))

#create a function to check if the absolute value of t_0 is less than that of t_* (within the interval [-t_*, t_*])
def interval_check(t_0,t_star):
    if t_0 > t_star:
        return False
    elif t_0 <= t_star:
        if t_0 >= (-1*t_star):
            return True
        elif t_0 < (-1*t_star):
            return False

#check if t_0 is in the interval for this example question
print("Is t_0 within the interval bound by negative and positive t_star?")
print(interval_check(t_0(mean(scores),mu_0,st_dev(scores,mean(scores)),scores),find_t_star(0.95,(len(scores)-1))))

# The output is false, meaning that the null hypothesis is rejected & the true mean is NOT 75.
# Since the calculated t_0 is higher than the 95% probability range, the data shows that the new teaching technique increases test scores & therefore must be beneficial.