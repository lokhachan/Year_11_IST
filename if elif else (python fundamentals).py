#Computer programs usually respond to input from the user.
#The program will behave differently depending on what input
#it receives. IF statements allow your program to react to
#the input it receives.

#The most basic type of IF statement is shown below. If the
#condition is true, it will run the code underneath. If
#the condition is not true, it will not run that code.

name = "nikolai"

if name == "nikolai": #when you're asking IF something is equal to something else, you must use a double equal sign
    print("Hi, nikolai.")



#You can create more complex IF statements using ELIF, which
#is short for "else if". With elif, you can create multiple
#options for the if statement. In the example below, there
#are three possible names that will result in a "Hi" statement.
#You can have as many elifs as you want..

name = "derp"

if name == "nikolai":
    print("Hi, nikolai.")
elif name == "derp":
    print("Hi, derp.")
elif name == "kenny":
    print("Hi, kenny.")


#But what if none of the conditions are true? In the example
#above, if the name was "frank", nothing at all would happen.
#This might be ok.. but it's often useful to have an option
#that covers anything that doesn't match one of the conditions.
#That's where ELSE comes in!

name = "frank"

if name == "nikolai":
    print("Hi, nikolai.")
elif name == "derp":
    print("Hi, derp.")
elif name == "kenny":
    print("Hi, kenny.")
else: #if the name is anything other than nikolai, derp, or kenny, the code below will run
    print("Hi, stranger.")