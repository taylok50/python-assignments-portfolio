# Import needed packs for choosing numbers at random & plotting the solution set.
import matplotlib.pyplot as plt
import random

# State the location of the vertices of an equilateral triangle.
vertices = [(0,0), (1,0), (0.5,0.866)]

# Create a function to determine if a point (x, y) lies inside the triangle.
# This function calculates the area of the equilateral triangle
# & compares it to the area of 3 triangles formed between the chosen point & 2 vertices of the equilateral triangle.
# If the area of the equilateral triangle = the sum of the areas of the 3 new triangles,
# then the point is inside the equilateral triangle.
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    return A == A1 + A2 + A3

# Create a loop that requires the x- & y-coordinates of the point to be input.
# The loop uses the previously defined function to determine if the point is inside the triangle.
# If so, the coordinates are accepted.
# If not, it asks for a different set of coordinates & states why the previous ones won't work.
while True:
    try:
        seed_x = float(input("Enter the x-coordinate of the seed point: "))
        seed_y = float(input("Enter the y-coordinate of the seed point: "))
        if isInside(0, 0, 1, 0, 0.5, 0.866, seed_x, seed_y):
            print("Valid seed point entered.")
            break
        else:
            print("The point is not inside the triangle. Please try again.")
    except ValueError:
        print("Invalid input. Please numerical values.")

# Create a point using the coordinates given & an array of all points.
# Currently, the only point in the array is the starting point.
seed = (seed_x, seed_y)
points = [seed]

# Use a loop to receive an input to decide on the number of steps.
# The loop will accept any answer that is a positive integer.
# If the input is below zero or not an integer, it will request a different input.
while True:
    try:
        num_steps = int(input("Enter the number of steps: "))
        if num_steps > 0:
            print(f"Number of steps is set to {num_steps}.")
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please a positive integer.")

# Make a loop for which the number of iterations is equal to the step number entered.
# For each iteration, it chooses a random number between 0 & 2, which corresponds to one of the triangle's vertices.
# It defines the next point as the midpoint of the straight line connecting the most recent point & the chosen vertex.
# Midpoint = ((sum of x-values / 2), (sum of y-values / 2))
# This new point is added to the array of points.
for i in range(num_steps):
    next_vertex = vertices[random.randint(0,2)]
    next_point = (((points[-1][0] + next_vertex[0]) / 2), ((points[-1][1] + next_vertex[1]) / 2))
    points.append(next_point)

# Set up a scatterplot & plot all the points in the array.
def plot_solution(points):
    plt.scatter([p[0] for p in points], [p[1] for p in points], s=0.1)
    plt.show()
plot_solution(points)