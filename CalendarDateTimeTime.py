# Yitzhak Alvarez 2019

#imports the calendar
import calendar
import datetime
import time
import pytz
print()#-> this prints out empty spaces

#prints out the integer value of what the first weekday is, starting with (6) Sunday. Ex: Monday is 0, Tuesday is 1... etc.

calendar.setfirstweekday(calendar.SUNDAY)

#prints out the specified month
print(calendar.month(2019, 8))
print()

#prints out the specified month in array form
print(calendar.monthcalendar(2019, 8))
print()

#prints out the specified year
print(calendar.calendar(2019))
print()

#time
start = time.time()
now = time.localtime()
now = time.asctime(now)
print (now)
print()

today = datetime.date.today()
print(today)
print() 

birthday = datetime.date(1998, 10, 8)
print(birthday)
print() 

#find days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)
print()

#adding 10 days to current day
tdelta = datetime.timedelta(days = 10)
print(today - tdelta)
print()

print(today.day)
print()

#prints out the weekday, Friday (4)
print(today.weekday())
print()

# Monday = 0, Sunday = 6

print(datetime.time(7, 2, 20, 15))
print()
#datetime.date (Y, M, D)
#datetime.time (h, m, s, ms)
#datetime.datetime(Y, M, D, h, m, s, ms)

#Adds 10 hrs to current days
hour_delta = datetime.timedelta(hours = 10)
print(datetime.datetime.now() + hour_delta)
print()

datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_eastern = datetime_today.astimezone(pytz.timezone('US/Eastern'))

print(datetime_eastern)
print()

for tz in pytz.all_timezones:
  print(tz)

#string formatting with dates 
#2019 - 08 - 02 -> August 02, 2019
#strftime (f = formatting) 
print(datetime_eastern.strftime('%B %d, %Y'))
print()

#August 02, 2019 -> datetime(2019, 8, 2)
#strptime (p = parsing)
datetime_thing = datetime.datetime.strptime('August 02, 2019', '%B %d, %Y')
print(repr(datetime_thing))
print()