def first(word):
	print word[0]
	return word[0]
def last(word):
	print word[-1]
	return word[-1]	
def middle(word):
	print word[1:-1]
	return word[1:-1]
def is_palindrome(wor):
	l = len(wor)
	print l
	print wor[l-1]
	i=0
	#x = -1
	while(wor):
		if (wor[i]==wor[l-1]):	
			i = i + 1
			l = l - 1
			print 's'
		else:
			print 'd'
			break
		
			


first('malayalam')
middle('malayalam')
last('malayalam')
is_palindrome('malayam')
