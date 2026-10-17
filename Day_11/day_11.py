import math

# 1. Add two numbers
def add_two_numbers(a, b):
    return a + b


# 2. Area of a circle
def area_of_circle(r):
    return math.pi * r * r


# 3. Add all numbers (arbitrary arguments)
def add_all_nums(*args):
    for num in args:
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            return "Error: All arguments must be numbers."
    return sum(args)


# 4. Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# 5. Check season
def check_season(month):
    month = month.strip().lower()

    seasons = {
        "autumn": ["september", "october", "november"],
        "winter": ["december", "january", "february"],
        "spring": ["march", "april", "may"],
        "summer": ["june", "july", "august"]
    }

    for season, months in seasons.items():
        if month in months:
            return season.capitalize()

    return "Invalid month"


# 6. Calculate slope
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)


# 7. Solve quadratic equation
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "Not a quadratic equation"

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solutions"

    if discriminant == 0:
        return [-b / (2*a)]

    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)

    return [root1, root2]


# 8. Print each list item
def print_list(items):
    for item in items:
        print(item)


# 9. Reverse a list using a loop
def reverse_list(items):
    reversed_items = []

    for item in items:
        reversed_items.insert(0, item)

    return reversed_items


# 10. Capitalize list items
def capitalize_list_items(items):
    return [item.capitalize() for item in items]


# 11. Add an item to a list
def add_item(items, item):
    new_list = items.copy()
    new_list.append(item)
    return new_list


# 12. Remove an item from a list
def remove_item(items, item):
    new_list = items.copy()

    if item in new_list:
        new_list.remove(item)

    return new_list


# 13. Sum all numbers from 1 to n
def sum_of_numbers(n):
    return sum(range(1, n + 1))


# 14. Sum all odd numbers from 1 to n
def sum_of_odds(n):
    total = 0

    for number in range(1, n + 1):
        if number % 2 != 0:
            total += number

    return total


# 15. Sum all even numbers from 1 to n
def sum_of_even(n):
    total = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            total += number

    return total


# Test the functions
if __name__ == "__main__":
    print("1.", add_two_numbers(5, 3))
    print("2.", round(area_of_circle(5), 2))
    print("3.", add_all_nums(1, 2, 3, 4))
    print("4.", convert_celsius_to_fahrenheit(25))
    print("5.", check_season("December"))
    print("6.", calculate_slope(1, 2, 3, 6))
    print("7.", solve_quadratic_eqn(1, -3, 2))

    print("8. List items:")
    print_list([1, 2, 3])

    print("9.", reverse_list([1, 2, 3, 4, 5]))
    print("10.", capitalize_list_items(["apple", "mango"]))
    print("11.", add_item(["Potato", "Milk"], "Meat"))
    print("12.", remove_item(["Potato", "Mango", "Milk"], "Mango"))
    print("13.", sum_of_numbers(5))
    print("14.", sum_of_odds(10))
    print("15.", sum_of_even(10))
