def remove_duplicate(a):
	k = 0
	b = []
	c = []
	for i in range(5):
		j = 1
		if(a[i]!=a[j]):
			b.append(a[i])
			j = j + 1
		else:
			if a[i] not in c:
				c.append(a[i])			
	print c+b

remove_duplicate([1,1,2,3,4])
