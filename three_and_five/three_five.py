def three_five():
    for test_num in range(1, 101):
        num = ""
        if test_num % 3 == 0:
            num += 'Three'
        if test_num % 5 == 0:
            num += 'Five'
        if num == "":
            num = str(test_num)

        print(num, end=' ')


if __name__ == "__main__":
    three_five()
