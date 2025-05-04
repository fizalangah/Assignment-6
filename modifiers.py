# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    
    def __init__(self):
        self.name = "fiza"
        self._selary = 500000
        self.__ssn = "ssn"

modifier =  Employee() 
print(modifier.name)
print(modifier._selary)

print(modifier.__ssn) #AttributeError: 'Employee' object has no attribute '__ssn'


