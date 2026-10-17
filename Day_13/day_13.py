
# 1. Filter negative numbers and zero using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

result = [n for n in numbers if n <= 0]

print("1.", result)


# 2. Flatten a list of lists into one list

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [n for sublist in list_of_lists for n in sublist]

print("2.", result)


# 3. Create a list of tuples using list comprehension

result = [
    tuple(n ** power for power in range(7))
    for n in range(11)
]

print("3.", result)


# 4. Convert countries into uppercase country, code, and city

countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

country_codes = {
    'Finland': 'FIN',
    'Sweden': 'SWE',
    'Norway': 'NOR'
}

result = [
    [country.upper(), country_codes[country], city.upper()]
    for group in countries
    for country, city in group
]

print("4.", result)


# 5. Convert countries into a list of dictionaries

result = [
    {'country': country.upper(), 'city': city.upper()}
    for group in countries
    for country, city in group
]

print("5.", result)


# 6. Convert names into concatenated strings

names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

result = [
    first + ' ' + last
    for group in names
    for first, last in group
]

print("6.", result)


# 7. Lambda functions to calculate slope and y-intercept

slope = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1) if x2 != x1 else None
)

y_intercept = lambda x, y, m: y - m * x

print("7. Slope:", slope(1, 2, 3, 6))
print("   Y-intercept:", y_intercept(1, 2, 2))
