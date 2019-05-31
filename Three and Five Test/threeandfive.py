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
