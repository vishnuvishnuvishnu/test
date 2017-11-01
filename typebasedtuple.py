class Point():
	#x = (a,b)
	def __init__(self,a=0,b=0):
		self.a = a
		self.b = b
		print self.a
		print self.b
	def __add__(self,other):
		obj = Point()
		if isinstance(other,tuple):
			obj.a = obj.a + self.a + other[0]
			obj.b = obj.b + self.b + other[1]
			return obj.a,obj.b

start= Point(2,1)
star = (1,4)
print start + star
