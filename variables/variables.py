# ============================================================
# PYTHON VARIABLES
# Basic to Advanced Practice
# ============================================================


# ============================================================
# LEVEL 1 — FUNDAMENTALS
# ============================================================

# Q1. Create a variable containing your name.

name = "Mahima"
print(name)


# Q2. Create variables for your name, age, and course.

name = "Mahima"
age = 21
course = "Data Science"

print(name)
print(age)
print(course)


# Q3. Print the value and data type of a variable.

name = "Mahima"

print("Value:", name)
print("Data type:", type(name))


# Q4. Create variables containing different values.

student_name = "Mahima"
age = 21
height = 5.4
is_student = True

print(student_name)
print(age)
print(height)
print(is_student)


# ============================================================
# LEVEL 2 — BASIC PRACTICE
# ============================================================

# Q5. Assign multiple variables in one statement.

name, age, city = "Mahima", 21, "Kathmandu"

print(name)
print(age)
print(city)


# Q6. Assign the same value to multiple variables.

x = y = z = 100

print(x)
print(y)
print(z)


# Q7. Update the value of a variable.

score = 50

print("Original score:", score)

score = 85

print("Updated score:", score)


# Q8. Create variables and calculate a total.

price = 500
quantity = 3

total = price * quantity

print("Total:", total)


# ============================================================
# LEVEL 3 — INTERMEDIATE PRACTICE
# ============================================================

# Q9. Calculate the average of three marks.

mark1 = 80
mark2 = 75
mark3 = 90

total_marks = mark1 + mark2 + mark3
average = total_marks / 3

print("Total:", total_marks)
print("Average:", average)


# Q10. Swap the values of two variables.

a = 10
b = 20

a, b = b, a

print("a:", a)
print("b:", b)


# Q11. Calculate the area of a rectangle.

length = 10
width = 5

area = length * width

print("Area:", area)


# Q12. Calculate the final salary.

basic_salary = 35000
allowance = 5000
deduction = 2000

final_salary = basic_salary + allowance - deduction

print("Final salary:", final_salary)


# ============================================================
# LEVEL 4 — ADVANCED PRACTICE
# ============================================================

# Q13. Use variables to calculate a discounted price.

original_price = 2500
discount_percentage = 15

discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount

print("Original price:", original_price)
print("Discount:", discount_amount)
print("Final price:", final_price)


# Q14. Calculate the total and average marks of five subjects.

python = 85
database = 80
statistics = 90
web_development = 75
data_analysis = 88

total = (
    python
    + database
    + statistics
    + web_development
    + data_analysis
)

average = total / 5

print("Total marks:", total)
print("Average marks:", average)


# Q15. Convert age from years into months and days.

age_years = 21

age_months = age_years * 12
age_days = age_years * 365

print("Age in months:", age_months)
print("Approximate age in days:", age_days)


# Q16. Calculate electricity cost.

units = 150
cost_per_unit = 12.5

electricity_bill = units * cost_per_unit

print("Electricity bill:", electricity_bill)


# ============================================================
# LEVEL 5 — REAL-WORLD PRACTICE
# ============================================================

# Q17. Create a student profile using variables.

student_name = "Mahima"
student_id = "DS021"
age = 21
course = "Data Science"
marks = 87.5
passed = True

print("\nStudent Profile")
print("-------------------------")
print("Name:", student_name)
print("Student ID:", student_id)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)
print("Passed:", passed)


# Q18. Calculate a shopping bill.

item_price = 1200
quantity = 2
discount_percentage = 10

subtotal = item_price * quantity
discount = subtotal * discount_percentage / 100
final_amount = subtotal - discount

print("\nShopping Bill")
print("-------------------------")
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final amount:", final_amount)


# Q19. Calculate employee net salary.

basic_salary = 40000
bonus = 5000
tax = 3000
insurance = 1000

gross_salary = basic_salary + bonus
net_salary = gross_salary - tax - insurance

print("\nSalary Details")
print("-------------------------")
print("Gross salary:", gross_salary)
print("Net salary:", net_salary)


# ============================================================
# LEVEL 6 — CHALLENGE
# ============================================================

# Q20. Calculate the total cost of a trip.

transport = 5000
hotel = 8000
food = 4000
activities = 2500

total_trip_cost = transport + hotel + food + activities

print("\nTrip Cost")
print("-------------------------")
print("Transport:", transport)
print("Hotel:", hotel)
print("Food:", food)
print("Activities:", activities)
print("Total trip cost:", total_trip_cost)


# Q21. Calculate the final amount after tax and discount.

product_price = 5000
discount_rate = 10
tax_rate = 13

discount = product_price * discount_rate / 100
price_after_discount = product_price - discount

tax = price_after_discount * tax_rate / 100
final_amount = price_after_discount + tax

print("\nFinal Purchase Calculation")
print("-------------------------")
print("Original price:", product_price)
print("Discount:", discount)
print("Tax:", tax)
print("Final amount:", final_amount)


# Q22. Create a complete student result calculation.

student_name = "Mahima"

subject1 = 85
subject2 = 90
subject3 = 78
subject4 = 88
subject5 = 92

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5
percentage = (total_marks / 500) * 100

print("\nStudent Result")
print("-------------------------")
print("Student:", student_name)
print("Total marks:", total_marks)
print("Average:", average_marks)
print("Percentage:", percentage)