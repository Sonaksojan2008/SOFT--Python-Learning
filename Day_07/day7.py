# Day 7 - Sets

# Level 1

# Given set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set
print("Length:", len(it_companies))

# 2. Add Twitter
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# 3. Add multiple IT companies
it_companies.update(['Intel', 'HP', 'Dell'])
print("After adding companies:", it_companies)

# 4. Remove one company
it_companies.remove('HP')
print("After removing HP:", it_companies)

# 5. Difference between remove and discard
# remove() gives an error if the item is not found
# discard() does not give an error if the item is not found

it_companies.discard('Nokia')

print("Final companies:", it_companies)


# Level 2

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. Join A and B
print("A union B:", A | B)

# 2. Intersection
print("A intersection B:", A & B)

# 3. Is A subset of B?
print("A is subset of B:", A.issubset(B))

# 4. Are A and B disjoint?
print("A and B are disjoint:", A.isdisjoint(B))

# 5. Join A with B and B with A
print("A union B:", A | B)
print("B union A:", B | A)

# 6. Symmetric difference
print("Symmetric difference:", A ^ B)

# 7. Delete sets
del A
del B


# Level 3

# 1. Convert ages to a set
ages = [19, 20, 18, 19, 21, 20, 18, 22]

ages_set = set(ages)

print("Ages list:", ages)
print("Ages set:", ages_set)
print("Length of list:", len(ages))
print("Length of set:", len(ages_set))


# 2. Data types
print("String: characters inside quotes")
print("List: ordered and changeable")
print("Tuple: ordered and unchangeable")
print("Set: unordered and unique")


# 3. Unique words
sentence = "I am a teacher and I love to inspire and teach people."

words = sentence.split()
unique_words = set(words)

print("Words:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
