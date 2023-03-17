import datetime as libtime

old = libtime.datetime(1970, 1, 1)

now = libtime.datetime.now()

total_seconds1 = (now - old).total_seconds()
total_seconds2 = total_seconds1
total_seconds1 = '{:,}'.format(total_seconds1)

scientific_number = '{:.2e}'.format(total_seconds2)

print("Seconds since January 1, 1970:",
      total_seconds1[:-2], "or", scientific_number, "in scientific notation")
print(now.strftime("%b %d %Y"))
