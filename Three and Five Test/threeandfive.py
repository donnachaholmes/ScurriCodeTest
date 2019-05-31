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


def nicer_way(lower_limit, upper_limit):
    upper_limit += 1
    string_list = []
    for test_num in range(lower_limit, upper_limit):
        if test_num % 3 == 0 and test_num % 5 == 0:
            string_list.append('ThreeFive ')
        elif test_num % 3 == 0:
            string_list.append('Three ')
        elif test_num % 5 == 0:
            string_list.append("Five ")
        else:
            string_list.append(str(test_num) + " ")

        if test_num % 10 == 0:
            string_list.append('\n')

    return "".join(string_list)


print('\n')
print(nicer_way(1, 100))
