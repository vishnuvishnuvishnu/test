class Point():
	#x = (a,b)
	def __init__(self,a=0,b=0):
		self.a = a
		self.b = b
		print self.a
		print self.b
	def __add__(self,other):
		obj = Point()
		if isinstance(other,Point):
			obj.a = obj.a + self.a + other.a
			obj.b = obj.b + self.b + other.b
			return obj.a , obj.b

start = Point(9,4)
dur = Point(4,5)
print start + dur
