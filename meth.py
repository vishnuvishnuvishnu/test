class Time(object):
	def print_time(time):
		print '%.2d:%.2d:%.2d' %(time.hour,time.minute,time.second)
	def increment(self , seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
	def time_to_int(times):
		minutes = times.hour * 60 + times.minute
		seconds = minutes * 60 + time.second
		return seconds
	def int_to_time(seconds):
		times = Time()
		minutes, times.second = divmod(seconds, 60)
		times.hour, times.minute = divmod(minutes, 60)
		return times
time = Time()
times = Time()
time.hour = 5
time.minute = 33
time.second = 43
Time.print_time(time)
end = times.increment(1232)
end.print_time()

