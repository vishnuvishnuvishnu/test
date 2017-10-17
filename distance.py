import math
class Point(object):
	print "hai"


blank = Point()
blank.x = 10
blank.y = 5
print blank.x
print blank.y

def distance_between_points(a,b):
	print '(%g,%g)' %(blank.x,blank.y)
	distance = math.sqrt(blank.x**2+blank.y**2)
	print distance	

distance_between_points(blank.x,blank.y)
