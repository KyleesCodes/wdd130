print('Hello World!')
#This is how to make a comment in python! Don't confuse this with html or javascript
#ctrl kc will turn a line into a comment, while ctrl ku will uncomment a line

sentence= 'look at how this is printed!'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('o'))
print(sentence.title())

#All below format codes will run the same way in python 3 and below, but the last is for python 3
    #output = 'Hello, ' + first_name + ' ' + last_name
    #output = 'Hello, {} {}'.format(first_name, last_name)
    #output = 'Hello, {0} {1}'.format(first_name, last_name)
    #(python 3 only) output = f'Hello, {first_name} {last_name}'

#For math: 
    # + = addition
    # - = subtraction
    # * = multiplication
    # / = division
    # // = divide and drop remainder
    # % = remainder
    # ** = exponent
    #To make a math segment print like a string, you'll write the segment as str(name_of_math_here) into the print function
    #When assigning an output, adding '' around numbers will make it a string and won't be able to use math functions
    #Input value will always come back as a string
    #The int function will turn the input into a whole integer and float will turn it into a floating number (something with decimals)
    #If you want to print a number in a string, you can use:
    #print(f'The number is {number}.')
    #Another way to format is:
    #print('There are {} cars on the road.'.format(car_count))
    #In a format string, you define the precision, or number of decimals to display, by putting a :.2f after the variable name (changing the 2 to whichever amount you'd like).
    #You can tell the computer to display the number in scientific notation, or "exponent" notation by using :.3e after your variable, where 3 defines the precision and e indicates that you are using exponent notation.
    #In any case, when you want to display large numbers to the user, you may want to display it with commas or underscores. This is done by using either :, or :_ after the variable name.
    #In order to use code from this library in your program, you'll need to import or include it. You do this by putting the code import math at the top of your program.
    #math.ceil(value)—Rounds value up to the next whole number, the "ceiling."
    #math.floor(value)—Rounds value down to the next whole number.
    #math.exp(value)—Raises e to the power of value.
    #math.sin(value)—Computes the trigonometry sine function of value in radians.

#For if...else:
    #Your code needs the ability to take different actions based on different conditions:
        #if price >= 1.00:
        #    tax = .07
        #    print(tax)
        #else:
        #    tax = 0
        #    print(tax)
    #Can write as:
        #if price >= 1.00:
        #    tax = .07
        #else:
        #    tax = 0
        #print(tax)
    #> = greater than
    #< = less than
    #>= = greater than or equal to
    #<= = less than or equal to
    #== = is equal to
    #!= = is not equal to
    #You can add formats to if...else statements to prevent user errors
    #You may need to set multiple if statements to check multiple coditions, so change if to elif
    #With elif, you are able to set multiple conditions AND an else statement
    #If one if statement shares the same outcome as another, you can write:
        #if province ==  'Alberta'\
        #    or province == 'Nunavut':
        #     tax = 0.05
    #If you have a list of possible values to check, you can use:
        #if province in('Alberta',\
        #               'Nunavut','Yukon'):
        #    tax = 0.05
    #If a condition requires multiple conditions to be met, you can nest if statements with else on the same structure of the outer if statement
    #Sometimes you can combine conditions with AND instead of nesting if statements
    #If you need to remember the results of a condition check later in your code, use Boolean variables as flags
        #if gpa >= .85 and lowest_grade >= .70:
            #honour_roll = True
        #else:
            #honour_roll = False
        #later on in your code:
        #if honour_roll:
            #print('Well done')

            #if x > 5 and y > 10:
            # This happens if both conditions are true
            #if x > 5 or y > 10:
            # This happens if either one of the conditions (or both!) are true
            #if x > 5 and y > 10 and word == "taco":
            # This happens if all three conditions are true
    #The and condition takes precedence over the or condition, so if you want to mix them and have the or condition happen first, you need to use parentheses:
        #if (x > 5 or x < -5) and y > 10:
        # In this case, x can either be greater than 5 or less than negative 5, and y must
        # always be greater than 10
        #if x > 5 or x < -5 and y > 10:
        # Without parentheses, the x < -5 and y > 10 conditions go together and both must be
        # true, unless x > 5, in which case the whole statement is true

    # To check if x is either 5 or 6, you might be tempted to write:
        #if x == 5 or 6:
        # INCORRECT: This does not work!

    # You must write them both out:
        #if x == 5 or x == 6:
        # This is the correct way to check
    # To check if either first_name or last_name is Scott you might be tempted to write:
        #if first_name or last_name == "Scott":
        # INCORRECT: This does not work!

    # You must write them both out:
        #if first_name == "Scott" or last_name == "Scott":
        # This is the correct way to check

#For loops:
    #tip = float(input())
    #while tip < 0:
        #print('Sorry, that is not a valid tip amount.')
        #tip = float(input())
        # # jump back to line 3

    #print(f"You have tipped ${tip:.2f}.")

    #for name in ['Christopher', 'Susan']:
        #print(name)
    
    #for index in range(0,2):
        #print(index)

    #names = ['Christopher', 'Susan']
    #index = 0
    #while index < len(names):
        #print(names[index])
        # #Change the condition!!
        #index = index + 1

    #To easily create a range of numbers, you can do: numbers = range(10) for a range of 0-9
    #To start with a different number, you provide two values to the range function. If you provide two numbers, it will start with the first one and continue up until (but not including) the second one.
    #If you provide three values to the range function, it will use the third number as the "step size" or in other words the number to count by.

    #You can nest loops!

#For lists:
    #list_name = []

    #list_name.append()  will add whatever is in parenthesis at the end of the list

    #example: 
        #clients = []

        #new_client = ''
        #while new_client != 'quit':
            #new_client = input('What is the name of the client? ')
            #clients.append(new_client)

        #for client in clients:
            #print(client)

#For internal data use:
    #To open files in python, you can use the code open("") to open an internal file you want to implement in your code, like a .txt file.
    #To open file course.txt it would look like courses_file = open("course.txt")
    #You need to set the opened file as a variable
    #To iterate through the file line by line, you can use:
        #for line in courses_file:
            #print(line)

    #You need to close a file when you are done with it. Will look something like variable.close()

    #Additionally you can write the full code as below:
        #with open("course.txt") as courses_file:
            #for line in courses_file:
                #print(line)
    #This method gets rid of the need to close a file since when it is done iterating through the code inside it will automatically close and move on

#Splitting strings:
    #This method will convert the white space into a split in a list:
        #colors = "red green blue yellow"

        #color_parts = colors.split()
    #If you place something in the () for split, it will then split it based on what string is in the () instead of white space

#Removing white space from strings:
    #This method will remove recurring white space from a string at the beginning or end:
        #name = "Kylee Tallman       "

        #clean_name = name.strip()

        #print(f"-----{clean_name}-----"")
    #You can also rename it to the same variable

#Reading files and parsing strings:
    #with open("course.txt") as courses_file:
        #for line in courses_file:
            #parts = line.split(",")
            #print(line)

    #If you change the print(line) to print(parts[0]) it will only print the names (CSE110, WDD301, etc.) and then changing the [] to 1 will print the grades (99.8, 82.3, etc.)

        #with open("course.txt") as courses_file:
        #for line in courses_file:
            #parts = line.split(",")
            #name = parts[0]
            #grade = float(parts[1])
            #bonus_grade = grade + 3
            #print(f"{name} - Grade: {grade}, after bonus: {bonus_grade})

        #Each line will be printed with an extra line in between because there is an invisible \n at the end of each line. To get rid of it, add .strip() to the fist varialbe in the if statement