# First solution is just to use a straight forward loop in a specified range of 100 integers
def simple():
    print('**** Straight Forward Function ****\n')
    count = 0
    for i in range(1, 101):
        # If the condition of the int being divisible by both 3 and 5 is met - we print ThreeFive
        if i % 3 == 0 and i % 5 == 0:
            print('ThreeFive'),
        # If the condition of the int being divisible by 3 is met - we print Three;
        elif i % 3 == 0:
            print('Three'), ;
        # If the condition of the int being divisible by 5 is met - we print Five;
        elif i % 5 == 0:
            print('Five'), ;
        # Otherwise - We just print the integer as it is not divisible by either three or 5
        else:
            print(i), ;

        # I use a count of 10 per line before moving to a new line just so it looks a bit nicer in the terminal
        count += 1
        if count == 10:
            count = 0
            print('\n'), ;


# A bit of a nicer way of doing it is to define a function that takes two arguments and displays this as needed
def nicer_way(lower_limit, upper_limit):
    # Let the user know the range of numbers being examined
    print('Displaying all the digits in the range {} to {}.\n'.format(lower_limit, upper_limit))
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

    # Next, I join the list of all values in the list and return as a string
    return "".join(string_list)


# Call the simple way of doing this task
simple()

print('\n')
print('**** Function that takes two arguments ****')
# Call the nicer way with the number range given in the task
print(nicer_way(1, 100))
