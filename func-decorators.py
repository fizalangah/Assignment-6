# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

class log_function_call:
    def __init__(self,func):
        self.func= func
        
    def __call__(self, *args, **kwds):
        print("function is being called")
        return self.func(*args, **kwds)
        

@log_function_call
def say_hello(name,fname):
    print("hi I am say hello function",name,fname)

say_hello("fiza",fname= "gm")
  