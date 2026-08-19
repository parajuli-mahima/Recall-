# PYTHON DATA TYPES
# Basic to Advanced Practice

# LEVEL 1 — FUNDAMENTALS

# Q1. Identify the data type of an integer.

age = 21

print(age)
print(type(age))


# Q2. Identify the data type of a float.

height = 5.6

print(height)
print(type(height))


# Q3. Identify the data type of a string.

name = "Mahima"

print(name)
print(type(name))


# Q4. Identify the data type of a Boolean.

is_student = True

print(is_student)
print(type(is_student))


# Q5. Identify the data type of None.

result = None

print(result)
print(type(result))

# LEVEL 2 — BASIC DATA TYPES

# Q6. Create variables using different basic data types.

name = "Mahima"
age = 21
height = 5.6
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))


# Q7. Create an integer and a float.

number = 100
price = 99.50

print(type(number))
print(type(price))


# Q8. Create two Boolean values.

is_logged_in = True
has_permission = False

print(type(is_logged_in))
print(type(has_permission))


# Q9. Create a complex number.

number = 3 + 4j

print(number)
print(type(number))

# LEVEL 3 — COLLECTION DATA TYPES

# Q10. Identify the type of a list.

skills = ["Python", "SQL", "Excel", "Tableau"]

print(skills)
print(type(skills))


# Q11. Identify the type of a tuple.

coordinates = (27.7172, 85.3240)

print(coordinates)
print(type(coordinates))


# Q12. Identify the type of a set.

numbers = {1, 2, 3, 4, 5}

print(numbers)
print(type(numbers))


# Q13. Identify the type of a dictionary.

student = {
    "name": "Mahima",
    "age": 21,
    "course": "Data Science"
}

print(student)
print(type(student))


# Q14. Create different collection types.

skills_list = ["Python", "SQL"]
skills_tuple = ("Python", "SQL")
skills_set = {"Python", "SQL"}
student_dict = {"name": "Mahima", "age": 21}

print(type(skills_list))
print(type(skills_tuple))
print(type(skills_set))
print(type(student_dict))

# LEVEL 4 — TYPE CONVERSION

# Q15. Convert a string into an integer.

age = "21"

age = int(age)

print(age)
print(type(age))


# Q16. Convert a string into a float.

price = "99.50"

price = float(price)

print(price)
print(type(price))


# Q17. Convert an integer into a string.

number = 100

number = str(number)

print(number)
print(type(number))


# Q18. Convert a number into a Boolean.

number = 1

result = bool(number)

print(result)
print(type(result))


# Q19. Convert a list into a tuple.

numbers = [10, 20, 30]

numbers = tuple(numbers)

print(numbers)
print(type(numbers))


# Q20. Convert a tuple into a list.

numbers = (10, 20, 30)

numbers = list(numbers)

print(numbers)
print(type(numbers))


# Q21. Convert a list into a set.

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
print(type(unique_numbers))

# LEVEL 5 — TYPE CHECKING

# Q22. Use type() to check the exact type.

value = 25

print(type(value))
print(type(value) == int)


# Q23. Use isinstance() to check a data type.

age = 21

print(isinstance(age, int))
print(isinstance(age, str))


# Q24. Check multiple data types.

name = "Mahima"
age = 21
marks = 85.5

print(isinstance(name, str))
print(isinstance(age, int))
print(isinstance(marks, float))


# Q25. Check whether a value is a list.

skills = ["Python", "SQL"]

print(isinstance(skills, list))

# LEVEL 6 — MUTABLE AND IMMUTABLE TYPES

# Q26. Modify a list.

skills = ["Python", "SQL", "Excel"]

skills[1] = "Power BI"

print(skills)


# Q27. Understand tuple immutability.

languages = ("Python", "SQL", "Java")

# The following would cause an error:
# languages[0] = "C++"

print(languages)


# Q28. Compare list and tuple.

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(type(my_list))
print(type(my_tuple))

# LEVEL 7 — MIXED DATA TYPES

# Q29. Store different data types in one list.

student = [
    "Mahima",
    21,
    87.5,
    True
]

print(student)

for item in student:
    print(item, type(item))


# Q30. Create a student record using mixed data types.

student = {
    "name": "Mahima",
    "age": 21,
    "marks": 87.5,
    "passed": True,
    "subjects": ["Python", "SQL", "Statistics"]
}

print(student)

# LEVEL 8 — ADVANCED TYPE PRACTICE

# Q31. Track the type after converting a value.

value = "100"

print("Original:", value, type(value))

value = int(value)

print("After integer conversion:", value, type(value))

value = float(value)

print("After float conversion:", value, type(value))

value = str(value)

print("After string conversion:", value, type(value))


# Q32. Remove duplicate values by converting a list to a set.

data = [10, 20, 20, 30, 30, 40, 40]

unique_data = set(data)

print("Original:", data)
print("Unique:", unique_data)


# Q33. Convert the unique values back into a list.

data = [1, 2, 2, 3, 3, 4]

unique_data = set(data)
unique_list = list(unique_data)

print(unique_list)
print(type(unique_list))


# Q34. Create a nested data structure.

student = {
    "name": "Mahima",
    "details": {
        "age": 21,
        "city": "Kathmandu"
    },
    "skills": ["Python", "SQL", "Power BI"]
}

print(student)
print(type(student))


# LEVEL 9 — REAL-WORLD PRACTICE

# Q35. Create a complete employee record.

employee = {
    "name": "Mahima",
    "age": 21,
    "salary": 45000.50,
    "is_active": True,
    "skills": ["Python", "SQL", "Excel"]
}

print(employee)

print("\nData Types:")
for key, value in employee.items():
    print(key, ":", type(value))


# Q36. Create a product record.

product = {
    "name": "Laptop",
    "price": 85000.00,
    "quantity": 2,
    "available": True
}

print(product)

# LEVEL 10 — CHALLENGE

# Q37. What are the final value and data type?

value = "50"

print(value)
print(type(value))

value = int(value)

print(value)
print(type(value))

value = value + 25

print(value)
print(type(value))

value = str(value)

print(value)
print(type(value))


# Q38. Convert a list containing duplicate values
# into a unique tuple.

numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)
result = tuple(unique_numbers)

print(result)
print(type(result))


# Q39. Create a complete student data structure.

student = {
    "name": "Mahima",
    "age": 21,
    "marks": 88.5,
    "passed": True,
    "subjects": ["Python", "Database", "Statistics"],
    "address": ("Kathmandu", "Nepal")
}

print(student)

for key, value in student.items():
    print(key, "=>", value, "|", type(value))


# Q40. FINAL DATA TYPE CHALLENGE

x = "100"
y = 50
z = 2.5

print(type(x))
print(type(y))
print(type(z))

x = int(x)

result = x + y + z

print("Result:", result)
print("Final data type:", type(result))