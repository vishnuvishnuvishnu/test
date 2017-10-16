def has_duplicate(a):
	for i in range(5):
		for j in range(5):
			if (a[i]!=a[j]):
				j= j+1
			else:
				print "True"

has_duplicate([1,2,3,4,5])
