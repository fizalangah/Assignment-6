# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count_num = 0

    def __init__(self):
        # self.count_num = count_num
        Counter.count_num += 1


    @classmethod
    def display(cls):
        print(f"Total count: {cls.count_num} .")
        

obj1 = Counter()

obj2 = Counter()

Counter.display()