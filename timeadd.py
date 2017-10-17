class Time(object):
	print "Time"
time = Time()
time.hour = raw_input("Enter the value of hour\t:")
time.minute = raw_input("Enter the minute value\t:")
time.second = raw_input("Enter the second value\t:")
time.hour1 = raw_input("Enter the value of hour 1\t:")
time.minute1 = raw_input("Enter the value of minute1 \t:")
time.second1 = raw_input("Enter the value of second1\t:")
print time.hour,":",time.minute,":",time.second
print time.hour1,":",time.minute1,":",time.second1

if(time.hour > time.hour1):
	print True
elif(time.hour == time.hour1):
	if(time.minute>time.minute1):
		print True
	elif(time.minute==time.minute1):
		if(time.second>time.second1):
			print True
		elif(time.second==time.second1):
			print 'equal'
		else:
			print False
	else:
		print False
else:
	print False
