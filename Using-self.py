# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details. 


# Solution:
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"my Name is {self.name} and i got {self.marks} marks")


student1 = Student("fiza",91)  
student1.display()         
    