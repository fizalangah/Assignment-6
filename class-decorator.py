# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# ✅ Class Decorator to Add greet() Method
class add_greeting:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, *args, **kwargs):
        # Add a greet method dynamically
        def greet(self):
            return "Hello from Decorator!"
        
        setattr(self.greeting, "greet", greet)
        return self.greeting(*args, **kwargs)

@add_greeting
class Person:
    def say_hello(self):
        return "Hello"

# ✅ Create object
cl = Person()

# ✅ Check methods
print(cl.say_hello())        
print(cl.greet())            
