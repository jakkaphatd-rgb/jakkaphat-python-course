"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
name = input("Enter your name: ")
age_input = input("Enter your age: ")
phone = input("Enter your phone number: ")
 
name_valid = all(
    word.isalpha() for word in name.split()
) and bool(name.strip())
 
 
if age_input.isdigit():
    age = int(age_input)
    age_valid = 18 <= age <= 65
else:
    age = 0
    age_valid = False
 
phone_valid = len(phone) == 10 and phone.isdigit()
 
print("\nValidation Results:")
 
if name_valid:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid")
 
if age_valid:
    print("Age: Valid ({} years old)".format(age))
else:
    print("Age: Invalid (must be between 18-65)")
 
if phone_valid:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (must contain exactly 10 digits)")
 
if name_valid and age_valid and phone_valid:
    if age <= 30:
        age_group = "Young Adult (18-30)"
    elif age <= 45:
        age_group = "Middle Adult (31-45)"
    else:
        age_group = "Older Adult (46-65)"
 
    print("\nFormatted Information:")
    print("Name: {}".format(name.upper()))
    print("Age Group: {}".format(age_group))
    print("Phone: +91-{}".format(phone))