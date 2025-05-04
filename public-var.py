
# 3. Public Variables and Methods
#  Assignment:
#  Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    public_var = "Toyota"

    def start(self):
        print(f"Car brand is: {self.public_var}.")
        
car = Car()
print(car.public_var)
car.start()
