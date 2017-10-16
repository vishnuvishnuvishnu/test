def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t,2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)
x = raw_input("Enter the t value \t")
y = raw_input("Enter the length value \t")
z = raw_input("Enter the n value \t")
draw(int(x),int(y),int(z))

