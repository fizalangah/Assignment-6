# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplies:
    def __init__(self,factor):
        
        self.factor = factor
         
    def __call__(self, value):
        # self.value = value
       if value % self.factor == 0:
          return self.factor * value
       else:
          return f"This value is not multiply by {self.factor}!"
       

mul = Multiplies(2)     

print(callable(mul))

print(mul(9))
