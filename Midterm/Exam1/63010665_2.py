if __name__ == '__main__':
    number = int(input("Input : "))
    if number <= 0 :
        print('!!!Please enter number greater than zero!!!')
    print(''
          '')
    stars = 1
    spaces = 2 * number - 2

    for _ in range(number):  #top
        for _ in range(stars):
            print('*', end="")
        for _ in range(spaces):
            print(' ', end="")
        for _ in range(stars):
            print('*', end="")
        stars += 1
        spaces -= 2
        print()

    stars -= 1
    spaces += 2
    for _ in range(number-1):  #bottom
        stars -= 1
        spaces += 2
        for _ in range(stars):
            print('*', end="")
        for _ in range(spaces):
            print(' ', end="")
        for _ in range(stars):
            print('*', end="")

        print()