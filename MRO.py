# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def Show(self):
        print("hello i am fiza, A")
        
class B(A):
    
    def Show(self):
        print("hello i am fiza ,B")

class C(A):
    def Show(self):
        print("hello i am fiza ,C")

class D(B,C):
     pass

d = D()
d.Show()