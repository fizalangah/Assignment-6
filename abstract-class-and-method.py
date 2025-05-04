# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod

class Shape:
  @abstractmethod
  def area(self):   
    pass
  
class Rectangle(Shape):
  def __init__(self,h,w):
    self.h = h
    self.w = w
    
  def area(self):
    return self.h * self.w

shape1 = Rectangle(5,5) 
print(shape1.area())
