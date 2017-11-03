class kangaroo():
	def __init__(self):
		self.pouch_contents = []
	def put_in_pouch(self,other):
		#print other
		self.pouch_contents.append(other)
		return self.pouch_contents
	def __str__(self):
		return self.pouch_contents

start = kangaroo()
print start.put_in_pouch(4)
		
		

