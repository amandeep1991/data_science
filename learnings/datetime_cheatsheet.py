import datetime


# Generate Dates
dt = datetime.datetime(1990, 1, 1)
end = datetime.datetime(2018, 12, 31, 0, 0, 0)
step = datetime.timedelta(hours=24)
result = []
while dt < end:  result.append(dt.strftime('%Y-%m-%d %H:%M:%S')); dt += step;
print(result)