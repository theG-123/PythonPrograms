import math

# Taking input from the user
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return midpoint_x, midpoint_y

# Calculate distance
distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the two points is: {distance:.2f}")

# Calculate midpoint
midpoint = calculate_midpoint(x1, y1, x2, y2)
print(f"The midpoint of the two points is: {midpoint}")
