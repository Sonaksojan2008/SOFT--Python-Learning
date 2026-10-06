for i in range(11):
    print(i)

    i = 0

while i <= 10:
    print(i)
    i += 1

for i in range(10, -1, -1):
    print(i)

    i = 10

while i >= 0:
    print(i)
    i -= 1

for i in range(1, 8):
    print("#" * i)

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

for i in range(11):
    print(i, "x", i, "=", i * i)

    languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for language in languages:
    print(language)

for i in range(0, 101, 2):
    print(i)