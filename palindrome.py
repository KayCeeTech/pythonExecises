if __name__ == '__main__':
    words = input("Enter a words: ")

    index = 0
    counter = 0

    while index < len(words) // 2:
        if words[index] == words[len(words) - index - 1]:
            counter += 1

        index += 1

    if counter == len(words) // 2:
        print("It is a palindrome number")

    else:
        print("It is not a palindrome number")
