# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed. legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

# 3. Create a student dictionary 
student = {
    'first_name': 'Sona',
    'last_name': 'Sojan',
    'gender': 'Female',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'C++', 'Java'],
    'country': 'India',
    'city': 'Thrissur',
    'address': {
        'street': '123 Main St',
        'zip_code': '10001'
    }

    print("Student dictionary:", student)

    # 4. Get the length of the student dictionary
    print("Length of student dictionary:", len(student))

    # 5. Get the value of skills and check the data type, 
    print('Skills:', student['skills'])
    print('Data type of skills:', type(student['skills']))

    # 6. Add one skill to the skills list
    student['skills'].append('JavaScript')
    print('Updated skills:', student['skills'])

    #7. Get the dictionary keys as a list
    keys = list(student.keys())
    print('keys:', keys)

    #8. Get the dictionary values as a list
    values = list(student.values())
    print('values:', values)

    # 9. Change the dictionary to a list of tuples 
    items = list(student.items())
    print('List of tuples:', items)

    #10. Delete one of the items in the dictionary
    del student['marital_status']
    print('Updated student dictionary after deleting marital_status:', student)

    # 11. Delete one of the dictionaries
    del dog

    print('Dog dictionary deleted.')



