
from datetime import datetime, date, time, timedelta

# 1. Get the current day, month, year, hour, minute and timestamp
now = datetime.now()

print("Current day:", now.day)
print("Current month:", now.month)
print("Current year:", now.year)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current timestamp:", now.timestamp())


# 2. Format the current date and time
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date and time:", formatted_date)


# 3. Convert the time string to a datetime object
time_string = "5 December, 2019"
converted_time = datetime.strptime(time_string, "%d %B, %Y")
print("Converted date:", converted_time)


# 4. Calculate the time difference between now and New Year
now = datetime.now()
next_new_year = datetime(now.year + 1, 1, 1)
time_difference = next_new_year - now

print("Time until New Year:", time_difference)


# 5. Calculate the time difference between 1 January 1970 and now
start_date = datetime(1970, 1, 1)
now = datetime.now()
time_difference = now - start_date

print("Time since 1 January 1970:", time_difference)


# 6. Uses of the datetime module
print("Uses of the datetime module:")
print("1. Time series analysis")
print("2. Getting timestamps of activities in an application")
print("3. Adding timestamps to blog posts")


