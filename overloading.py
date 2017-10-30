class Point():
	print "hai"
	head = 'I am'
	def __str__(self):
		return self.head
	def __init__(x=0 ,y=0):
		print x,y
	def __add__(self,other):
		tot = self.__str__() + other.__str__()
		return tot
	__init__(7)
spr = Point()
qwe = Point()
print str(spr)
print spr + qwe
