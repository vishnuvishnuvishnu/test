def is_triangle(a,b,c):
	p = a + b
	q = b + c
	r = a + c
	if (p < c or q < a or r < b):
		print "You cant form a triangle with these sides"
		print a
		print b
		print c
	else:
		print "Can possible to form a triangle with these sides "
		print a
		print b
		print c
x= raw_input("Enter the value of the side a ")
y= raw_input("Enter the value of the side b ")
z= raw_input("Enter the value of the side c ")
is_triangle(int(x),int(y),int(z))
