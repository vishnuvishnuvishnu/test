class Point():
	print "What is this"
blank = Point()
print blank
blank.x = 3.0
blank.y = 4.0
print blank.x
print blank.y

class Rectangle(object):
	print "Atributes are width,height and corner"
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
print box.width
print box.height
print box.corner.x
print box.corner.y

