#a) define the gradient descent function:
import numpy as np #needed for mathematical processes
def gradient_descent(x0, y0, f, grad_f, alpha, num_iterations):
    x,y = x0, y0 #ensure x & y begin at given starting point
    i = 0 #start from iteration number 0
    for i in range(num_iterations): #create loop to change x & y vals in each step so that function approaches min
        grad_x, grad_y = grad_f(x,y) #define partial derivatives within gradient vector
        x = x - alpha*grad_x #take step along x-axis in direction that causes function to decrease
        y = y - alpha*grad_y #take step along y-axis in direction that causes function to decrease
        i = i + 1  # increase counter before moving to next iteration
        if np.abs(grad_x)<0.01 and np.abs(grad_y)<0.01: #if gradient gets very small in both x & y directions...
            i = num_iterations - 1 #skip to final iteration
    return x,y #return coordinates of function min as output

#b) find min values of f_1(x,y) = x**2 + y**2:
#define the function
def fun_1(x,y):
    return x**2 + y**2
#define the gradient as a vector containing both partial derivatives
def grad_f_1(x,y):
    grad_x = 2*x #calculated by hand
    grad_y = 2*y #calculated by hand
    return grad_x, grad_y
#apply gradient descent to test cases
print(gradient_descent(0.1,0.1,fun_1,grad_f_1,0.1,10))
print(gradient_descent(-1,1,fun_1,grad_f_1,0.01,100))

#c) find min values of f_2(x,y) = 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2):
#define the function
def fun_2(x,y):
    return 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)
#define the gradient as a vector containing both partial derivatives
def grad_f_2(x,y):
    grad_x = 2*x*(np.exp(-x**2-(y-2)**2)+2*np.exp(-x**2-(y+2)**2)) #calculated by hand
    grad_y = -1*np.exp(-x**2-(y-2)**2)*(-2*y+4)-2*np.exp(-x**2-(y+2)**2)*(-2*y-4) #calculated by hand
    return grad_x, grad_y
#apply gradient descent to test cases
print(gradient_descent(0,1,fun_2,grad_f_2,0.01,10000))
print(gradient_descent(0,-1,fun_2,grad_f_2,0.01,10000))
#notice that both test cases result in the same x-val output & different y-val outputs (same magnitude, opposite signs)
#plot the function
from mpl_toolkits import mplot3d #needed for 3D plots
import matplotlib.pyplot as plt #needed for general plotting
X=np.linspace(-5,5,100) #define range of x-vals to plot
Y=np.linspace(-5,5,100) #define range of y-vals to plot
x,y=np.meshgrid(X,Y) #creates rectangular grid (xy-plane)
z= fun_2(x,y) #equate z-value with function output
fig = plt.figure() #create plot as figure
ax = plt.axes(projection='3d') #create 3D axes
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none') #plot the function
plt.show() #display the plot