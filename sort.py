def is_sort(a):
	i = 0
	j = 1
	for i in range(5) :
		for j in range(5) :
			if (a[i]< a[j]):
				temp = a[j]
				a[j] = a[i]
				a[i] = temp
	print a

is_sort([5,2,8,7,1])

