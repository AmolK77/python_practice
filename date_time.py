# import dateteme module
from  datetime import date
from  datetime import datetime,timedelta
from datetime import time


my_date=date(1996,12,11)
print(my_date)

#get todays month,date,year
today=date.today()
print("today",today.day)
print("current month ",today.month)
print("current year",today.year)

#get date from timestamp
#getting datetime from timestamp
date_time=datetime.fromtimestamp(1887639468)
print("date time from timestamp",date_time)


#convert date to string
str=date.isoformat(today)
print("String representation",str)
print(type(str))


print("Now i wwill play With time")

#calling the constrctor
my_time=time(13,24,56)

print("Entered time",my_time)


#calling constructor with one argument
my_time=time(minute=12)
print("time with one argument",my_time)



#get hours,minute ,seconds and microseconds
Time=time(11,34,56)
print("Hour=",Time.hour)
print("minute =",Time.minute)
print("Seconds=",Time.second)
print("Microsecond",Time.microsecond)


#convert time_object to string object
T=time(12,24,36,1212)

#convetting time object  to string
str_time=T.isoformat()
print("string representation",str_time)


print("now i will play with timedalta")

# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print("initial_date",ini_time_for_now)


#calculating future date
#for 2 years
future_date_after_two_year=ini_time_for_now + timedelta(days=730)
future_date_after_two_days=ini_time_for_now +timedelta(days=2)

#print future date and days
print("future date after 2 years",future_date_after_two_year)
print("future date after 2 days",future_date_after_two_days)

futer_date_after_7_days=ini_time_for_now +timedelta(days=7)
print("Future date after 7 days",futer_date_after_7_days)

#difference between two date and time

days_after_7=ini_time_for_now +timedelta(days=7)




#datetime format
#ex1
now=datetime.now()
s=now.strftime("%A %m   %Y ")
print("Example 1",s)

# Example 2
s2 = now.strftime("%a %m %y")
print('\nExample 2:', s2)


# strptime() creates a datetime object from the given string.




