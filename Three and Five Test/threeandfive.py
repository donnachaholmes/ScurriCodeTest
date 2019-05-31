# The first solution to the problem goes through a range of numbers 1-100
# and tests if the conditions for Three, Five and ThreeFive are met
# There is a variable that assigns the test number as a string -
# if one of the conditions are met, this changes to Three, Five or ThreeFive
# At the end of each loop we print the value of the num variable
# if 10 numbers have been examined, we go to a new line
for test_num in range(1, 101):
    num = str(test_num)
    if test_num % 3 == 0 and test_num % 5 == 0:
        num = 'ThreeFive'
    elif test_num % 3 == 0:
        num = 'Three'
    elif test_num % 5 == 0:
        num = 'Five'

    print(num, end=' ')

    if test_num % 10 == 0:
        print('\n', end='')

print('\n')

# The second solution works on the same principles as the first solution except
# we use a list and add the value to the list at the end of each cycle of the
# loop - Then after the loop has finished, we print the list with join function
string_list = []
for test_num in range(1, 101):
    num = str(test_num) + ' '
    if test_num % 3 == 0 and test_num % 5 == 0:
        num = 'ThreeFive'
    elif test_num % 3 == 0:
        num = 'Three'
    elif test_num % 5 == 0:
        num = 'Five'
    string_list.append(num)

    if test_num % 10 == 0:
        string_list.append('\n')

print(''.join(string_list))
