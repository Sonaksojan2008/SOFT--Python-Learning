# DAY 6 - TUPLES

# Level 1

# 1. Create an empty tuple
empty_tuple = ()
print(empty_tuple)


# 2. Create a tuple containing names of sisters and brothers
sisters = ("Anu", "Meenu")
brothers = ("Akhil", "Arjun")

print("Sisters:", sisters)
print("Brothers:", brothers)


# 3. Join brothers and sisters tuples
siblings = brothers + sisters
print("Siblings:", siblings)


# 4. How many siblings do you have?
print("Number of siblings:", len(siblings))


# 5. Add father and mother and assign to family_members
family_members = siblings + ("Ravi", "Sheela")
print("Family members:", family_members)


# Level 2

# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members

print("Siblings:", siblings)
print("Father:", father)
print("Mother:", mother)


# 2. Create fruits, vegetables and animal products tuples
fruits = ("Apple", "Banana", "Orange")
vegetables = ("Carrot", "Tomato", "Potato")
animal_products = ("Milk", "Egg", "Cheese")

food_stuff_tp = fruits + vegetables + animal_products
print("Food stuff tuple:", food_stuff_tp)


# 3. Change food_stuff_tp tuple to a list
food_stuff_lt = list(food_stuff_tp)
print("Food stuff list:", food_stuff_lt)


# 4. Slice out the middle item or items
middle = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    print("Middle items:", food_stuff_lt[middle-1:middle+1])
else:
    print("Middle item:", food_stuff_lt[middle])


# 5. Slice out first three and last three items
print("First three items:", food_stuff_lt[:3])
print("Last three items:", food_stuff_lt[-3:])


# 6. Delete food_stuff_tp tuple completely
del food_stuff_tp


# 7. Check if an item exists in tuple
nordic_countries = (
    "Denmark",
    "Finland",
    "Iceland",
    "Norway",
    "Sweden"
)

print("Is Estonia a Nordic country?", "Estonia" in nordic_countries)
print("Is Iceland a Nordic country?", "Iceland" in nordic_countries)