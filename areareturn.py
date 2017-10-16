import math
def area(radius):
	pi = 3.14
	return math.pi*radius**2
r = raw_input("Enter the radius: \t ")
area(int(r))
