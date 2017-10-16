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

while(time.hour > time.hour1):
	print "true"
	break
else:
 print "Falsex"	
	
