#You can use the input() function to let the user input data into your program.

favourite_food = input("What is your favourite food? ")
print(f"Your favourite food is {favourite_food}? Gross.")


#By default, anything the user types into an input() will be received as a string.
#So if you want to do math on the user's input, you'll need to convert it to a number of some sort.
#If you try to do mathematical calculations on a string, it will either give you an error or
#a weird, unexpected result.

number_to_double = input("Type a number and I'll double it: ")
number_to_double = int(number_to_double) #this converts number_to_double into an integer
doubled_number = number_to_double * 2 #this does the calculation
print(f"Your double number is {doubled_number}.") #and here's the output