#a FUNCTION is a piece of code that only executes when it is told to.
#This is called 'calling' a function.
#Functions usually have () at the end.

#Python comes with lots of built-in functions.
#For example, print() is a function.
print("hello world")


#Another example of a built-in function is the int() function
#The int() function converts a string or float to an integer.
my_integer = int("10") #this assigns my_integer a value of 10
my_other_integer = int(21.12) #using int() on a float will round it


#We can also create our own functions. This is very useful.
#Below is a function named say_hi(). When it is called, it will
#print "hi" to the console.
def say_hi(): #this creates the say_hi() function
    print("hi") #and this is the code that will run when it is called

say_hi() #and we call the function here


#Functions can also take ARGUMENTS. An argument is a piece of
#data that is sent to the function. The function can then use
#that piece of data to do.. something.

def say_hi_to(name): #this function takes one argument, which is "name"
    print(f"Hi, {name}!") #this print statement uses the argument to say "Hi, " followed by whatever name it was given

say_hi_to("Spongebob") #when this function is called, the argument "Spongebob" will be sent to the function.
#the output of this will be "Hi, Spongebob!"


#Functions can take more than one argument. We can modify the code above..

def say_hi_to(firstname, lastname): #this function takes two arguments, "firstname" and "lastname"
    print(f"Hi, {firstname} {lastname}!")

say_hi_to("Spongebob", "Squarepants")
#So the output of this function call would be "Hi, Spongebob Squarepants!"


#And functions can also 'return' a value. Basically the function can output a value that can be used somewhere else in the program.

def square_this_number(number_to_square):
    squared_number = number_to_square * number_to_square #this calculates the square of the number
    return squared_number #this line 'returns' the value that was calculated above

result = square_this_number(10) #this calls the function with an argument of 10. so the result is 100.
print(result)