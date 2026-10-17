
import random
import string

# LEVEL 1

# 1. Generate a six-character random user ID
def random_user_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))


# 2. Generate user IDs using user input
def user_id_gen_by_user():
    length = int(input("Enter number of characters: "))
    count = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits

    for i in range(count):
        user_id = ''.join(random.choices(characters, k=length))
        print(user_id)


# 3. Generate a random RGB color
def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"rgb({red},{green},{blue})"


# LEVEL 2

# 1. Generate hexadecimal colors
def list_of_hexa_colors(n):
    colors = []

    for i in range(n):
        color = '#'
        for j in range(6):
            color += random.choice('0123456789abcdef')
        colors.append(color)

    return colors


# 2. Generate RGB colors
def list_of_rgb_colors(n):
    colors = []

    for i in range(n):
        colors.append(rgb_color_gen())

    return colors


# 3. Generate hexa or RGB colors
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type"


# LEVEL 3

# 1. Shuffle a list
def shuffle_list(items):
    new_list = items.copy()
    random.shuffle(new_list)
    return new_list


# 2. Generate seven unique random numbers
def unique_random_numbers():
    return random.sample(range(10), 7)


# TEST THE FUNCTIONS

print("1. Random user ID:", random_user_id())

print("\n2. Generate user IDs:")
user_id_gen_by_user()

print("\n3. RGB color:", rgb_color_gen())

print("\n4. Hexadecimal colors:", list_of_hexa_colors(3))

print("\n5. RGB colors:", list_of_rgb_colors(3))

print("\n6. Generate hexadecimal colors:")
print(generate_colors('hexa', 3))

print("\nGenerate RGB colors:")
print(generate_colors('rgb', 3))

print("\n7. Shuffled list:", shuffle_list([1, 2, 3, 4, 5]))

print("\n8. Seven unique numbers:", unique_random_numbers())

