# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    """A class that counts down from a given start number."""
    
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            current = self.current
            self.current -= 1
            return current    

# Example usage:
countdown = Countdown(5)    
for number in countdown:
    print(number)  # Output: 5, 4, 3, 2, 1, 0