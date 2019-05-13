# First solution is just to use a straight forward loop in a specified range of 100 integers
def simple():
    print('**** Straight Forward Function ****\n')
    count = 0
    for i in range(1, 101):
        # If the condition of the int being divisible by both 3 and 5 is met - we print ThreeFive
        if i % 3 == 0 and i % 5 == 0:
            print 'ThreeFive',
        # If the condition of the int being divisible by 3 is met - we print Three;
        elif i % 3 == 0:
            print 'Three', ;
        # If the condition of the int being divisible by 5 is met - we print Five;
        elif i % 5 == 0:
            print 'Five', ;
        # Otherwise - We just print the integer as it is not divisible by either three or 5
        else:
            print i, ;

        # I use a count of 10 per line before moving to a new line just so it looks a bit nicer in the terminal
        count += 1
        if count == 10:
            count = 0
            print'\n', ;


# A bit of a nicer way of doing it is to define a function that takes two arguments and displays this as needed
def nicer_way(lower_limit, upper_limit):
    # Let the user know the range of numbers being examined
    print'Displaying all the digits in the range {} to {}.\n'.format(lower_limit, upper_limit)
    upper_limit += 1
    # I create an empty list to add the values to before printing
    string_list = []
    count = 0
    # Loop through the range based on the two limits supplied to the function
    for test_num in range(lower_limit, upper_limit):
        # If the condition of the int being divisible by both 3 and 5 is met - we add ThreeFive to the list
        if test_num % 3 == 0 and test_num % 5 == 0:
            string_list.append('ThreeFive ')
        # If the condition of the int being divisible by 3 is met - we add Three to the list;
        elif test_num % 3 == 0:
            string_list.append('Three ')
        # If the condition of the int being divisible by 5 is met - we add Five to the list;
        elif test_num % 5 == 0:
            string_list.append("Five ")
        # Otherwise - We just add the integer as it is not divisible by either three or 5
        else:
            string_list.append(str(test_num) + " ")

        # I use a count of 10 per line before moving to a new line just so it looks a bit nicer in the terminal
        count+= 1
        if count == 10:
            count = 0
            string_list.append('\n')

    #Next, I join the list of all values in the list and return as a string
    return "".join(string_list)


# Call the simple way of doing this task
simple()

print'\n'
print('**** Function that takes two arguments ****')
# Call the nicer way with the number range given in the task
print(nicer_way(1, 100))

HELP = '''    Help:
    If the digit is divisible by 3, \'Three\' will be printed
    If the digit is divisible by 5, \'Five\' will be printed
    If the digit is divisible by both 3 and 5, \'ThreeFive\' will be printed\n
    First, you enter the lower limit (where to start, then you enter the upper limit(where to finish)
    RULES: The lower limit must be less than the upper limit, the values must be integers and they must be positive numbers\n
    To leave, enter \'QUIT\'
    To get help, enter\'HELP\'\n'''

print(HELP)

# I added a user interface that will allow the user to add their arguments as a range and perform the task required
while True:
    # Firstly we prompt for the lower limit - if the input is empty we loop back to the start and prompt for an int
    # If they enter 'quit' or 'QUIT' - The loop will break out and the program is finished
    # If they enter 'help' or 'HELP' - we display the help text above
    # We then normalise the data to make sure it is greater than 0 and an integer
    # The same thing will happen for when the upper limit is prompted
    # Finally, we make sure that the lower limit is less than the upper limit
    # Any errors here will result in a an error message being thrown and going back to the start of the loop
    lower_limit = raw_input('Enter a lower limit to investigate\n> ')
    if not lower_limit:
        print('Please enter an input')
        continue
    if lower_limit.lower() == 'quit':
        break
    if lower_limit.lower() == 'help':
        print(HELP)
        continue
    try:
        lower_limit = int(lower_limit)
    except ValueError as err:
        print('Input must be an int, please try again')
        continue
    if lower_limit <= 0:
        print('Lower Limit must be greater than 0')
        continue

    upper_limit = raw_input('Enter an upper limit investigate\n> ')
    if not upper_limit:
        print('Please enter an input')
        continue
    if upper_limit.lower() == 'quit':
        break
    try:
        upper_limit = int(upper_limit)
    except ValueError as err:
        print('Input must be an int, please enter an int, try again')
        continue
    if upper_limit <=0:
        print('Upper Limit must be greater than 0')
        continue

    if lower_limit >= upper_limit:
        print('Lower limit must be less than upper limit, try again')
        continue

    # When we have two good pieces of data to analyze, we send the ints to the function and process the data
    print(nicer_way(lower_limit, upper_limit))
