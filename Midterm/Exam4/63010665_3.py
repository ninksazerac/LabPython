comparison = 0
def swap(lis, x, last, lastNum):
    global comparison
    if x < 0:
        return lis, last
    else:
        lis, position = swap(lis, x-1, last, lastNum)

        if lis[last] < lis[x]:
            if lis[last] == lastNum:
                position = x
            temp = lis[last]
            lis[last] = lis[x]
            lis[x] = temp
            if x != 0:
                comparison += 1
        return lis, position

def insert(lis, num):
    if num == 0:
        return lis
    else:
        global comparison
        lis = insert(lis, num-1)
        last = num
        lastNum = lis[last]
        comparison += 1
        lis, position = swap(lis, num, last, lastNum)

    return lis

print(' *** Insertion sort ***')
input1 = [int(i) for i in input('Enter some numbers : ').split()]
y = len(input1)-1
lis = insert(input1,y)
print()
print(lis)
print('Data comparison = ', comparison)