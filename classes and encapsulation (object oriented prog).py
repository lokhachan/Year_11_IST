### This program includes a Dog class that can be used to create Dog objects.
### It's very limited in what it can do, though. We'll improve it soon.

# class Dog:
#     name = "Kenny"
#     breed = "chihuahua"
#
# my_dog = Dog()

# print(f"My dog is {my_dog.name} and it is a {my_dog.breed}.")




### This version uses a CONSTRUCTOR to help INSTANTIATE an object based on the class.
### Instantiate just means "create". When you INSTANTIATE an object, you are creating
### an INSTANCE of the class.
### This is better because it allows you to assign values to the attributes when
### you instantiate the object. This can be done by letting the user input() information
### about the object, for example.

# class Dog:
#     def __init__(self, name, breed): # this def __init__() section is a constructor
#         self.name = name
#         self.breed = breed
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
#
# my_dog = Dog(name, breed)
#
# print(f"Your dog is {my_dog.name} and it is a {my_dog.breed}.")



### This version includes a method. When that method is called, it will print the word "woof".

# class Dog:
#     def __init__(self, name, breed): # this def __init__() section is a constructor
#         self.name = name
#         self.breed = breed
#
#     def bark(self): # this is a method, which is just a function that's part of an object.
#         print("woof")
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
#
# my_dog = Dog(name, breed)
#
# print(f"Your dog is {my_dog.name} and it is a {my_dog.breed}.")
# my_dog.bark()



### This version includes ENCAPSULATION, which is one of the four fundamental characteristics
### of Object Oriented Programming. The attributes will be protected from anything outside of
### the object.

# class Dog:
#     def __init__(self, name, breed):
#         self.__name = name   # By adding __ before the attribute name, it becomes PRIVATE.
#         self.__breed = breed # That means it can't be viewed or modified from outside the object.
#
#     def bark(self): # this is a method, which is just a function that's part of an object.
#         print("woof")
#
#     def describe(self):
#         print(f"Your dog is {my_dog.__name} and it is a {my_dog.__breed}.")
#         # Because this is a method of the object, it can see the private attributes
#         # like my_dog.__name and my_dog.__breed
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
#
# my_dog = Dog(name, breed)
#
# my_dog.bark()
# my_dog.describe()



### Ok, but this is just dog stuff. Who cares about data security? Let's
### try an example where it actually matters: banking.



### This is a very basic way to do banking. Not flexible and not secure.

# my_account_balance = 1000
# my_account_id = "FREER1234"
# withdrawal_amount = int(input("How much would you like to withdraw? "))
# my_account_balance = my_account_balance - withdrawal_amount
# print(f"You withdrew {withdrawal_amount}")
# print(f"New balance: {my_account_balance}")




### This is a better way to do it. It uses a class to create an object
### that represents a bank account with a balance and an account id.
### There is a method that allows money to be withdrawn from the account.
### It's ok but still not very secure.

# class SavingsAccount():
#     def __init__(self, balance, account_id):
#         self.balance = balance
#         self.account_id = account_id
#
#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print(f"You withdrew {withdrawal_amount}")
#         print(f"New balance: {self.balance}")
#
# my_account = SavingsAccount(1000, "FREER1234")
#
# print(f"Current balance: {my_account.balance}")
#
# withdrawal_amount = int(input("How much would you like to withdraw? "))
#
# my_account.withdraw(withdrawal_amount)



### And here we have an even better version. It uses ENCAPSULATION to
### make sure the account balance can't be changed in an unexpected way.
### The balance and account_id attributes are private and can only be
### modified by methods in the savings account object. This helps to
### protect the data from other parts of the program messing with it.

# class SavingsAccount():
#     def __init__(self, balance, account_id):
#         self.__balance = balance
#         self.__account_id = account_id
#
#     def withdraw(self, withdrawal_amount):
#         if withdrawal_amount > 0:
#             self.__balance = self.__balance - withdrawal_amount
#             print(f"You withdrew {withdrawal_amount}")
#             print(f"New balance: {self.__balance}")
#         else:
#             print("Nice try! Please enter a positive number or I'll call the police..")
#
# my_account = SavingsAccount(1000)
#
# withdrawal_amount = int(input("How much would you like to withdraw? "))
# my_account.withdraw(withdrawal_amount)