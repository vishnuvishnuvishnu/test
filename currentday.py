from datetime import date
import calendar
given_date = date.today()
current_day=calendar.day_name[given_date.weekday()]
print current_day
