import sys

# sys.argv = list of command line parameters whose first value (0th indexed value) is file name
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])


import time

# using time() to display time since epoch
print("Seconds elapsed since the epoch are:",time.time())

# using gmtime() to return the time attribute structure
# Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a. GMT). When 'seconds' is not passed in, convert the current time instead.
print("Time calculated acc. to given seconds is:", time.gmtime()) # Current Time
print("Time calculated acc. to given seconds is:", time.gmtime(1539500000)) # passed seconds since epoch


time.gmtime(0)

time.gmtime().tm_year
time.gmtime()

time.gmtime().tm_sec

import time
print(time.time()) #returns seconds

start = time.time()

print("I'm doing a job.")
time.sleep(2) #seconds

end = time.time()
time_lapsed_in_seconds = end - start
print('Total Execution Time:', time_lapsed_in_seconds)




import time

now = time.localtime(time.time())

print(time.asctime(now))
print(time.strftime("%y/%m/%d %H:%M", now))
print(time.strftime("application_logs_%Y_%m_%d-%H_%M.log", now))
print(time.strftime("%a %b %d", now))
print(time.strftime("%c", now))
print(time.strftime("%I %p", now))
print(time.strftime("%Y-%m-%d %H:%M:%S %Z", now))

"my_application_.log"
"my_application.log"
"my_application.log"
"my_application.log"
"my_application.log"
"my_application.log"

import time
my_gmt_time = time.gmtime()

print("Year:",my_gmt_time.tm_year)
print("Month:",my_gmt_time.tm_mon)
print("Day:",my_gmt_time.tm_mday)
print("Hour:",my_gmt_time.tm_hour)
print("Min:",my_gmt_time.tm_min)
print("Sec:",my_gmt_time.tm_sec)
print("Weekday:",my_gmt_time.tm_wday)
print("YearDay:",my_gmt_time.tm_yday)


import datetime
x = datetime.datetime.now()
print(x)
print(type(x))
str(x)

x.microsecond

print(x.year)
print(x.day)
print(x.strftime("%A"))
print(x.weekday())
print(x.strftime("%a"))