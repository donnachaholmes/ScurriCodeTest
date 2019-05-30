for i in range(1, 101):
    num = str(i)
    if i % 3 == 0 and i % 5 == 0:
        num = 'ThreeFive'
    elif i % 3 == 0:
        num = 'Three'
    elif i % 5 == 0:
        num = 'Five'

    print(num, end=' ')

    if i % 10 == 0:
        print('\n', end='')


# A bit of a nicer way of doing it is to define a function that takes two arguments and displays this as needed
def nicer_way(lower_limit, upper_limit):
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
        count += 1
        if count == 10:
            count = 0
            string_list.append('\n')

    # Next, I join the list of all values in the list and return as a string
    return "".join(string_list)


print('\n')
print('**** Function that takes two arguments ****')
# Call the nicer way with the number range given in the task
print(nicer_way(1, 100))
