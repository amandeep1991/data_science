import sys
sys.argv # returns list whose first element is the file name and arguments starts from 2nd (index=1)

# Task 1: when n = 5, print below
# *
# **
# ***
# ****
# *****

# Task 2: when n = 6, print below
#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# Task 3: when n = 5, print Task 1 with mirror on x-axis
# Task 4: when n = 5, print Task 2 with mirror on x-axis

# Task #5: Create a calculator supporting +,-,/,* and ** operators from command line (Command Line Arguments).
# Command
# python calculator.py 2 + 3
# # output on console
# 2+3=5
#
# # Command
# python calculator.py 2 ** 3
# # output on console
# 2**3=8
#

import time

# 1 January, 12:00 am, 1970

#COMMENT using time() to display time since epoch
print("Seconds elapsed since the epoch are:",time.time())
# Seconds elapsed since the epoch are: 1539957935.6607878

# Converts seconds into different time details as key value pair.
now = time.localtime(time.time())
print(now)
now.tm_year
now.tm_year
# tm_year=2018, tm_mon=10, tm_mday=20, tm_hour=9, tm_min=55, tm_sec=9, tm_wday=5, tm_yday=293, tm_isdst=0

time.gmtime()
time.gmtime(1540009000)

print("It's starting..........")
time.sleep(2)
print('Started')

now = time.localtime(time.time())
print(time.asctime(now))
print(time.strftime("%y/%m/%d %H:%M", now))
print(time.strftime("%a %b %d", now))
print(time.strftime("%I %p", now))
print(time.strftime("%Y-%m-%d %H:%M:%S %Z", now))

print(time.strftime("MyNameIsKhan_%Y_%m_%d_%H_%M.log", now))

gm = time.gmtime()
print(gm.tm_year)
print(gm.tm_mon)
print(gm.tm_mday)
print(gm.tm_hour)
print(gm.tm_min)
print(gm.tm_sec)
print(gm.tm_wday)
print(gm.tm_yday)
print(gm.tm_isdst)

import datetime
# Class in datetime: date - Done
# Class in datetime: time
# Class in datetime: datetime
# Class in datetime: timedelta
# Class in datetime: tzinfo

datetime.datetime.now()

# import datetime
# datetime.date
# from datetime import date

x = datetime.datetime.now()
print(x.year)
# 2018
print(x.day)
print(x.strftime("%y/%m/%d %H:%M"))


import datetime

print(datetime.date(2018,10,19))
# 2018-10-19
print(datetime.date.today())
# 2018-10-19
print(datetime.date.fromtimestamp(time.time()))
print(datetime.date.fromtimestamp(0))
# 2018-10-19
print(datetime.date(2018,10,19).replace(year=2020))
# 2020-10-19
print(datetime.date(2018,10,20).weekday())
# 4
print(datetime.date(2018,10,20).ctime()) #Current local date
# Fri Oct 19 00:00:00 2018



#ERROR print(datetime.time(24,0,0,0))
#ERROR print(datetime.time(23,60,0,0))
print(datetime.time(23,59,0,0))
# 23:59:00
print(datetime.time(23,59,0,0).hour)
# 23



print(datetime.datetime(2018,10,20,9,30,32,222))
# 2018-10-20 09:30:32.000222

#COMMENT datetime.datetime.now() takes tzinfo as keyword argument but datetime.today() does not take any keyword arguments.
print(datetime.datetime.today())
# 2018-10-19 18:56:05.426560
print(datetime.datetime.now())
# 2018-10-19 18:56:05.426559

time_time = time.time()
type(time_time)
print(datetime.datetime.fromtimestamp(time_time))
time_time=100000.1000001
print(datetime.datetime.fromtimestamp(time_time))
# 2018-10-19 18:56:05.426560
print(datetime.datetime.today().replace(microsecond=1))
# 2018-10-19 18:56:05.000001
print(datetime.datetime.today().date())
# 2018-10-19
print(datetime.datetime.today().time())
# 18:56:05.426560
print(datetime.datetime.fromtimestamp(time.time()))
# 2018-10-19 18:56:05.426560
import pytz
print(datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata")).timetz())
# 18:56:05.426559
print(datetime.datetime.now(tz=pytz.timezone("America/Los_Angeles")).timetz())
# 06:26:05.426559
print(datetime.datetime.now().ctime())
# Fri Oct 19 18:56:05 2018
print(datetime.datetime.now().weekday())
# 4



import datetime
d1 = datetime.timedelta(seconds=10)
print((d1.days, d1.seconds, d1.microseconds))
d2 = timedelta(microseconds=1)
# (0, 10, 0)
d1 = d1-d2
print((d1.days, d1.seconds, d1.microseconds))
# (0, 9, 999999)

d1 = timedelta(seconds=-10)
print((d1.days, d1.seconds, d1.microseconds))
# (-1, 86390, 0)
d1=abs(d1)
print((d1.days, d1.seconds, d1.microseconds))
# (0, 10, 0)

print(str(d1)) # '-1 day, 23:59:59.999999' or  '0:00:00.000001'
# 0:00:10

print(d1.total_seconds()) # contains total number of seconds contained in the duration
# 10.0

dd = timedelta(days=900, seconds=900)
print(dd.days)
print(dd.seconds)



import datetime
naive = datetime.datetime.now()
print(naive.tzinfo)


import datetime
import pytz

d = datetime.datetime.now()
timezone = pytz.timezone("Asia/Kolkata")
d_aware = timezone.localize(d)
print(d_aware.tzinfo)
# Asia/Kolkata


import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
print(utc_now)
# 2018-10-19 14:16:33.163281+00:00
pst_now = utc_now.astimezone(pytz.timezone("America/Los_Angeles"))
print(pst_now)
# 2018-10-19 07:16:33.163281-07:00

print(pst_now == utc_now)
# True