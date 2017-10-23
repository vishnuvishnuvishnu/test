from datetime import date
import datetime
import calendar
given_date = date.today()
print given_date
current_day=calendar.day_name[given_date.weekday()]
print current_day
now = datetime.datetime.now()
print now.year
print now.month
print now.day
yr = int(raw_input('enter the year u were born: \t'))
print yr
age = now.year - yr
print "Ur age is",age
hour = int(raw_input("Hour(24hr) in which u born: "))
minute = int(raw_input("Minute in which u born: "))
second = int(raw_input("Second in which u born: "))
pen_hr = 24 - hour
pen_min = 60 - now.minute
pen_second = 60 - now.second
hour_dur = pen_hr
print hour_dur
minute_dur = pen_min
second_dur = pen_second
nxt_yr = now.year+1
print nxt_yr
mnt = int(raw_input("Enter the month in which u born: "))
dy = int(raw_input("enter the day in which u born: "))
dur = (date(nxt_yr,mnt,dy)-date(now.year,now.month,now.day)).days
print dur,'Days' ,hour_dur,'Hours' ,minute_dur,'Minute' ,second_dur,'Seconds'

