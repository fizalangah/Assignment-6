# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age: {age}. Age must be 18 or above.")

# Function that checks age and raises exception if needed
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Access granted. Age is valid.")

# Using try...except to handle the exception
try:
    check_age(18)
except InvalidAgeError as e:
    print("Error:", e)
