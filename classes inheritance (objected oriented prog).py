class Animal: # this is the PARENT CLASS
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def dance(self):
        print(f"{self.name} does a little dance.")

class Dog(Animal): # this is a CHILD CLASS
    def __init__(self, name, furryness):
        super().__init__(name) # this line allows the child class to inherit the name attribute from the parent class
        self.furryness = furryness

    def speak(self):
        print(f"{self.name} barks!")


my_animal = Animal("Steve") # this line INSTANTIATES the my_animal object
print(my_animal.name)
my_animal.speak()

my_dog = Dog("Mr Barky", "extremely furry") # this INSTANTIATES my_dog object based on the Dog child class
print(my_dog.name, my_dog.furryness) # it requires TWO arguments because the Dog child class has a furryness attribute that the parent class doesn't
my_dog.speak()
























# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} makes a sound.")
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         print(f"{self.name} barks!")
#
#     def eat(self):
#         print("I'm eating.")
#
#
#
# # Create instances of the classes
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")
#
#
# # Call the speak method on the instances
# animal.speak()
# dog.speak()