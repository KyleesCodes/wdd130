import datetime
    #Print timestamps to see how long sections of code take to run

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()

#Instead of copy and pasting code we can instead write a function

def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()

#def defines a function that you can later use repeatedly throughout your code

from datetime import datetime
#Imports the datetime class from the datetime library
def print_time():
    print('task completed')
    print(datetime.now())
    print()

#To pass the task name as a parameter:

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('first name assigned')

for x in range(0,10):
    print(x)
print_time('loop completed')

#

first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial + last_name_initial)

#We can use a def function here as well like so:

def get_inital(name):
    initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_inital(first_name)

last_name = input('Enter your last name: ')
last_name_initial = get_inital(last_name)

print('Your initials are: ' + first_name_initial + last_name_initial)

#With the return, we are then returned a value back. We then have to have a place to store the value, which is where the first_name_inital and last name i comes in.
#You can even skip placing the return value into a variable by calling it directly in statements.

def get_inital(name):
    initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
last_name_initial = get_inital(last_name)

print('Your initials are: ' + get_inital(first_name) + get_inital(last_name))

#

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = ('Enter your first name: ')
first_name_initial = get_inital(first_name, False)

print('Your initials are: ' + first_name_initial)

#By using boolean "False", we then tell the system that force_uppercase is not and it runs the else statement under the def function.
#You can also set a default parameter by adding =True or =Flase after ...name, force_upper. 
#Later on during the "your initials are" print statement, you can even change what the boolean is by typing ...force_uppercase=False, name=first_name) instead of ...first_name)

#A function is a group of statements that together perform one task. Broadly speaking, there are four types of functions in Python which are:

#   Built-in functions
#   Standard library functions
#   Third-party functions
#   User-defined functions

#A user-defined function is a function that is not a built-in function, a standard function, or a third-party function. A user-defined function is written by a programmer like yourself as part of a program. For some students the term “user-defined function” is confusing because the user of a program doesn’t define the function. Instead, the programmer (you) define user-defined functions. Perhaps a more correct term is programmer-defined function. Writing user-defined functions has several advantages, including:

#   making your code more reusable
#   making your code easier to understand and debug
#   making your code easier to change and add capabilities

