print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python")
print("Coding" + " " + "For" + " " + "All")
company = "Coding For All"
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])
print("Coding" in company)
print(company.replace("Coding", "Python"))

sentence12 = "Python for Everyone"
print(sentence12.replace("Everyone", "All"))
print(company.split())
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))
print(company[0])
last_index = len(company) - 1
print(last_index)

print(company[10])
pfe = "Python for Everyone"
words = pfe.split()
print(words[0][0] + words[1][0]+ words[2][0])

words2 = company.split()
print(words2[0][0] + words2[1][0] + words2[2][0])

print(company.index("C"))
print(company.index("F"))
print("Coding For All People".rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

print(sentence.rfind("because"))
print(sentence[31:54])

print(company.startswith("Coding"))
print(company.endswith("Coding"))

spaces_str = "   Coding For All      "
print(spaces_str.strip())

print("30 days of python".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("#".join(libraries))

print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

radius = 10
area = int(3.14 * radius ** 2)
print(f"The area of a circle with radius {radius} is {area}.")

print(f"8+6 = {8 + 6}")
print(f"8-6 = {8 - 6}")
print(f"8*6 = {8 * 6}")
print(f"8/6 = {8 / 6}")
print(f"8%6 = {8 % 6}")
print(f"8//6 = {8 // 6}")
print(f"8**6 = {8 ** 6}")















