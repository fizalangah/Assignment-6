# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Employee Name: {self.name}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.show_info()


# Create an independent Employee object
emp1 = Employee("Fiza Langah")

# Create a Department and pass the Employee object
dept1 = Department("IT", emp1)

# Display department and employee info
dept1.show_details()