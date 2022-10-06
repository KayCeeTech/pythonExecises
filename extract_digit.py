if __name__ == '__main__':
    number = input("Enter a number to extract: ")

    index = 0
    while index < len(number):
        print(number[len(number) - 1 - index], end=' ')

        index += 1
