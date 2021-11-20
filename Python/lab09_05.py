'''
Sort Subset
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /
1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม
โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้
1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก
ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import
อธิบาย Test Case 1:
[2]
[-1, 3]
[0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]
'''
def bubbleSortLength(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if len(subList[i]) > len(subList[i + 1]):
                # swapping len of subset
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList


def bubbleSortNum(subList):
    for loop in range(1, len(subList)):
        swap = False

        for i in range(len(subList) - loop):
            if subList[i] > subList[i + 1]:
                # swapping num of subset
                subList[i], subList[i + 1] = subList[i + 1], subList[i]
                swap = True

        if swap is False:
            break
    return subList


# korn code - knapsack
def subListSum(ans, lst, index=0, result=None, carry=None):  # knapsack style

    if result is None:  # init new list
        result = []
    if carry is None:
        carry = []

    if index >= len(lst):    # base case    # increasing to exceed len(lst)
        #print(carry)
        return result

    carry.append(lst[index])
    #print('assign Value', result, '===',carry, index)

    if sum(carry) == ans:   # sum of lst ... compare to answer
        result.append(carry.copy())     # copy because it pass by ref ...

    result = subListSum(ans, lst, index + 1, result, carry)  # recursive
    #print()
    #print('after recur1', result, '===', carry, index)
    carry.pop()
    #print('pop before recur2', result, '===', carry, index)
    #print()
    result = subListSum(ans, lst, index + 1, result, carry)  # recursive
    #print()
    #print('after recur2', result, '===', carry, index)
    #print()
    return result


ans, lst = input('Enter Input : ').split('/')
ans = int(ans)
lst = [int(i) for i in lst.split()]

subList = []

# 2/-2 3 1 -1 0 -3 2
lst = bubbleSortNum(lst)
subList = subListSum(ans, lst)

# print(subList)
if len(subList) != 0:
    for i in bubbleSortLength(subList):
        print(i)
else:
    print('No Subset')