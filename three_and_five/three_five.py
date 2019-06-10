for test_num in range(1, 101):
    num = str(test_num)
    if test_num % 3 == 0 and test_num % 5 == 0:
        num = 'ThreeFive'
    elif test_num % 3 == 0:
        num = 'Three'
    elif test_num % 5 == 0:
        num = 'Five'

    print(num, end=' ')
