import copy
class Rectangle():
	print "hai"
	

box = Rectangle()
box.width= 100.0
box.height = 200.0

box1 = copy.copy(box)
print box.width,box.height
print box1.width,box1.height


