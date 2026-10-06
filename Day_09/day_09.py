age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need", 18 - age, "more years to learn to drive.")

my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print("I am", difference, "years older than you.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print("You are", difference, "years older than me.")
else:
    print("We are the same age.")