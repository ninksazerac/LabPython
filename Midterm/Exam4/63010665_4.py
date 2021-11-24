count = 0
def shellSort(arr):
    n = len(arr)
    k = 8 // 2
    global count
    while k > 0:
        for i in range(k, n):
            temp = arr[i]
            l = i
            count += 1
            while l >= k and arr[l - k] > temp:
                count += 1
                arr[l] = arr[l - k]
                l -= k
            arr[l] = temp
        k //= 2
    return count

print(" *** Shell sort ***")
input_ = [int(x) for x in input("Enter some numbers : ").split(" ")]
r = shellSort(input_)
print()
print(input_)
print("Data comparison =  {}".format(r))