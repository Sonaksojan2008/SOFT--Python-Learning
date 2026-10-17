
from datetime import datetime, date, time

# 1. Get the current day, month, year, hour, minute and timestamp
now = datetime.now()

print("1. Current date and time:")
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())


# 2. Format the current date and time
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

print("\n2. Formatted date and time:")
print(formatted_date)


# 3. Change the time string to time
time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y")

print("\n3. String converted to datetime:")
print(time_object)


# 4. Calculate the time difference between now and New Year
current_time = datetime.now()
new_year = datetime(current_time.year + 1, 1, 1)

time_difference = new_year - current_time

print("\n4. Time left until New Year:")
print(time_difference)


# 5. Calculate the time difference between 1 January 1970 and now
start_date = datetime(1970, 1, 1)
current_time = datetime.now()

difference = current_time - start_date

print("\n5. Time difference since 1 January 1970:")
print(difference)


# 6. Uses of the datetime module
print("\n6. Uses of the datetime module:")
print("1. Time series analysis")
print("2. Recording timestamps of activities in applications")
print("3. Adding dates and times to blog posts")


