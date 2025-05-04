# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
     
    bank_name = "Bank Al Habib"
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        # print(name)



bank1 = Bank()
print(bank1.bank_name)
Bank.change_bank_name("Alied bank")
bank2 = Bank()
print(bank2.bank_name)
bank3 = Bank()
print(bank3.bank_name)








