
from functools import reduce

# Country list
countries = [
    "Estonia", "Finland", "Sweden", "Denmark", "Norway",
    "Iceland", "India", "Nigeria", "Kenya", "Ethiopia",
    "Australia", "Canada", "Japan", "Germany", "France",
    "New Zealand", "South Africa", "United States"
]

names = ["Sona", "Anu", "Amal"]
numbers = [1, 2, 3, 4, 5, 6]


# 1. Change countries to uppercase
print("1.", list(map(str.upper, countries)))


# 2. Square each number
print("2.", list(map(lambda n: n * n, numbers)))


# 3. Change names to uppercase
print("3.", list(map(str.upper, names)))


# 4. Countries containing 'land'
print("4.", list(filter(lambda c: "land" in c.lower(), countries)))


# 5. Countries having exactly six characters
print("5.", list(filter(lambda c: len(c) == 6, countries)))


# 6. Countries having six or more characters
print("6.", list(filter(lambda c: len(c) >= 6, countries)))


# 7. Countries starting with E
print("7.", list(filter(lambda c: c.startswith("E"), countries)))


# 8. Chain map, filter and reduce
result = reduce(
    lambda a, b: a + b,
    filter(lambda n: n % 2 == 0, map(lambda n: n * n, numbers))
)
print("8.", result)


# 9. Return only string items
def get_string_lists(items):
    return [item for item in items if isinstance(item, str)]

print("9.", get_string_lists([1, "Apple", "Mango", 2, "Orange"]))


# 10. Sum all numbers using reduce
print("10.", reduce(lambda a, b: a + b, numbers))


# 11. Concatenate the countries into a sentence
north_european = [
    "Estonia", "Finland", "Sweden",
    "Denmark", "Norway", "Iceland"
]

sentence = (
    reduce(lambda a, b: a + ", " + b, north_european[:-1])
    + ", and " + north_european[-1]
    + " are north European countries"
)
print("11.", sentence)


# 12. Find countries containing a pattern
def categorize_countries(pattern):
    return [c for c in countries if pattern.lower() in c.lower()]

print("12.", categorize_countries("land"))
print(categorize_countries("ia"))
print(categorize_countries("island"))
print(categorize_countries("stan"))


# 13. Count countries by starting letter
def count_countries_by_letter():
    result = {}

    for country in countries:
        letter = country[0].upper()
        result[letter] = result.get(letter, 0) + 1

    return result

print("13.", count_countries_by_letter())


# 14. Return first ten countries
def get_first_ten_countries():
    return countries[:10]

print("14.", get_first_ten_countries())


# 15. Return last ten countries
def get_last_ten_countries():
    return countries[-10:]

print("15.", get_last_ten_countries())

