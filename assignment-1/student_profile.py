# --------------------------------------------------------
# Lab Assignment 1: Student Profile Console App
# Author: prince
# Roll No: 2501060169prince
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# --------------------------------------------------------

print("\n" + "="*60)
print("🎓 Welcome to Student Profile Generator CLI")
print("="*60)
print("This tool will collect your details and generate your profile card.")
print("You will also learn Python basics like:")
print("- Variables\n- Data Types\n- Operators\n- String Functions\n- File Handling\n")

# --------------------------------------------------------
# Task 2: Input & Variables
# --------------------------------------------------------

full_name = input("Enter your full name: ")
roll_no = input("Enter your roll number: ")
program = input("Enter your program (e.g., BCA): ")
university = input("Enter your university name: ")
city = input("Enter your city: ")

age = int(input("Enter your age: "))   # Type conversion
hobby = input("Enter your hobby: ")

print("\n✅ Student Data Recorded Successfully!\n")

# --------------------------------------------------------
# Task 3: Python Operators Demonstration
# --------------------------------------------------------

print("="*60)
print("🔢 Python Operators Demonstration")
print("="*60)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic Operations
print("\n-- Arithmetic Operations --")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} // {num2} = {num1 // num2}")

# Assignment Operator
a = num1
a += 5
print("\n-- Assignment Operator Example --")
print(f"num1 += 5 → {a}")

# Comparison Operators
print("\n-- Comparison Operators --")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} == {num2} : {num1 == num2}")

# Logical Operators
print("\n-- Logical Operators --")
print(f"({num1} > {num2}) and ({num1} != {num2}) : {(num1 > num2) and (num1 != num2)}")

# Identity Operator
print("\n-- Identity Operators --")
print(f"num1 is num2 : {num1 is num2}")

# Membership Operator
print("\n-- Membership Operators --")
sample_string = full_name.lower()
print(f"'a' in your name? : {'a' in sample_string}")

# --------------------------------------------------------
# Task 4: String Operations & Methods
# --------------------------------------------------------

print("\n" + "="*60)
print("🔤 String Formatting & Methods Demo")
print("="*60)

print("Uppercase name:", full_name.upper())
print("Lowercase name:", full_name.lower())
print("Title case name:", full_name.title())
print("Name length:", len(full_name))
print("Replace a with @:", full_name.replace("a", "@"))

# --------------------------------------------------------
# Task 5: Student Profile Card Output
# --------------------------------------------------------

print("\n" + "-"*60)
print("          STUDENT PROFILE SYSTEM")
print("-"*60)

print(f"Name:            {full_name}")
print(f"Roll No:         {roll_no}")
print(f"Course:          {program}")
print(f"University:      {university}")
print(f"City:            {city}")
print(f"Age:             {age}")
print(f"Hobby:           {hobby}")

print("-"*60)
print("Welcome to Python Programming! ✅")
print("-"*60)

# --------------------------------------------------------
# Task 6: Bonus Task – Save Profile to File
# --------------------------------------------------------

save = input("\nDo you want to save your profile? (yes/no): ").lower()

if save == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("STUDENT PROFILE\n")
        file.write("-"*50 + "\n")
        file.write(f"Name: {full_name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Course: {program}\n")
        file.write(f"University: {university}\n")
        file.write(f"City: {city}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hobby: {hobby}\n")
        file.write("-"*50)

    print("\n✅ Profile saved to student_profile.txt")
else:
    print("\n✅ Profile not saved.")

print("\n🎯 Thank you for using Student Profile CLI!")