print("*** Fun with Drawing ***")


num = int(input("Enter input : "))
for i in range(num) :
    for j in range(num - i - 1) :
        print('.', end='')
    print('*', end='')
    for j in range((i * 2) - 1) :
        print('+', end='')
    if i == 0 :
        print('', end='')
    else :
        print('*', end='')
    for j in range((num - 1 - i) * 2 - 1) :
        print('.', end='')

    if i == num - 1 :
        print('', end='')
    else :
        print('*', end='')
    for j in range((i * 2) - 1) :
        print('+', end='')
    if i == 0 :
        print('', end='')
    else :
        print('*', end='')

    for j in range(num - i - 1) :
        print('.', end='')
    print('')
for i in range((num - 1) * 2) :
    for j in range(i + 1) :
        print('.', end='')
    print('*', end='')
    for j in range(-3 + ((num - 1) * 4) - (2 * i)) :
        print('+', end='')
    if i == (((num - 1) * 2) - 1) :
        print('', end='')
    else :
        print('*', end='')
    for j in range(i + 1) :
        print('.', end='')
    print('')


