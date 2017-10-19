class mul_time():
	print "T"

time = mul_time()
time.hour = float(raw_input("Enter the hour:\t"))
time.minute = float(raw_input("Enter the minute:\t"))
time.second =float(raw_input("Enter the seconds:\t"))
speed = float(raw_input("Enter the speed : \t"))

print time.hour

hour = time.hour + ((time.minute)/60) + ((time.second)/3600)
print hour

dist = hour * speed
print dist
