import sympy as sp #needed for differentiation

# Exercise 4a)
x, y = sp.symbols('x y') #define symbols
f = sp.exp(x) * sp.sin(y) + y**3 #define function
df_dx = sp.diff(f, x) #differentiate w respect to x
df_dy = sp.diff(f, y) #differentiate w respect to y
print("df_dx =", df_dx, "and df_dy =", df_dy) #print partial derivatives
print() #print blank line

# Exercise 4b)
g = x**2 * y + x * y**2 #define function
dg_dx = sp.diff(g, x) #differentiate w respect to x
dg_dy = sp.diff(g, y) #differentiate w respect to y
grad_vector = dg_dx, dg_dy #combine partial derivatives to create gradient vector
print("grad_vector =", grad_vector) #print general gradient vector expression
dg_dx_at_xval = dg_dx.subs(x, 1) #substitue 1 for x in partial derivative wrt x
dg_dx_at_point = dg_dx_at_xval.subs(y, -1) #substitue -1 for y in partial derivative wrt x
dg_dy_at_xval = dg_dy.subs(x, 1) #substitue 1 for x in partial derivative wrt y
dg_dy_at_point = dg_dy_at_xval.subs(y, -1) #substitue -1 for y in partial derivative wrt y
grad_vector_at_point = dg_dx_at_point, dg_dy_at_point #define gradient vector at (1, -1)
print("The gradient vector at (1, -1) is", grad_vector_at_point) #print value of gradient vector at (1, -1)
print() #print blank line

# Exercise 4c)
h = sp.log(x**2 + y**2) #define function
dh_dx = sp.diff(h, x) #calculate derivative wrt x
dh_dy = sp.diff(h, y) #calculate derivative wrt y
dh_dxx = sp.diff(dh_dx, x) #calculate 2nd derivative wrt x
dh_dyy = sp.diff(dh_dy, y) #calculate 2nd derivative wrt y
dh_dydx = sp.diff(dh_dx, y) #calculate mixed partial derivative wrt x, then y
dh_dxdy = sp.diff(dh_dy, x) #calculate mixed partial derivative wrt y, then x
print("The second partial derivative of h(x) with respect to x is", dh_dxx) #print 2nd derivative wrt x
print("The second partial derivative of h(x) with respect to y is", dh_dyy) #print 2nd derivative wrt y
print("The mixed second partial derivatives of h(x) are", dh_dydx, "and", dh_dxdy) #print mixed 2nd partial derivatives
# Notice that the mixed 2nd partial derivatives are identical.
# Since h(x) doesn't change if x & y are swapped, that means it is symmetric.
# Therefore, the partial derivatives wrt x & y are the same, except the variables are swapped.
# As a result, the mixed 2nd partial derivatives are identical.

# Exercise 4d)
import numpy as np #needed for creation of numerical function
import matplotlib.pyplot as plt #needed for plotting
j = x**3 - 3*x*y + y**3 #define function
j_func = sp.lambdify((x, y), j, 'numpy') #convert to numerical function
x_vals = np.linspace(-3, 3, 400) #define x-val inputs
y_vals = np.linspace(-3, 3, 400) #define y-val inputs
X, Y = np.meshgrid(x_vals, y_vals) #create xy-grid
Z = j_func(X, Y) #solve for j-val of all input vals in xy-grid
plt.contourf(X, Y, Z, levels=50, cmap='viridis') #create contour plot
plt.colorbar() #add legend
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$') #add title
plt.xlabel('$x$') #add x-axis label
plt.ylabel('$y$') #add y-axis label
plt.show() #show plot

# Exercise 4e)
k = x**2 - y**2 #define function
k_func = sp.lambdify((x, y), k, 'numpy') #convert to numerical function
x_vals = np.linspace(-3, 3, 400) #define x-val inputs
y_vals = np.linspace(-3, 3, 400) #define y-val inputs
X, Y = np.meshgrid(x_vals, y_vals) #create xy-grid
Z = k_func(X, Y) #solve for k-val of all input vals in xy-grid
plt.contourf(X, Y, Z, levels=50, cmap='viridis') #create contour plot
plt.colorbar() #add legend
plt.title('Contour plot of $k(x, y) = x^2 - y^2$') #add title
plt.xlabel('$x$') #add x-axis label
plt.ylabel('$y$') #add y-axis label
plt.show() #show plot