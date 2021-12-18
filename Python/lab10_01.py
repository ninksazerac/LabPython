'''
หัดใช้ Binary Search
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False
***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

'''
def bi_search(left, right, lst, key):
    if left <= right:
        mid = (left + right) // 2
        if lst[mid] < key:
            return bi_search(mid + 1, right, lst, key)
        elif lst[mid] > key:
            return bi_search(left, mid - 1, lst, key)
        else:
            return True
    return False


if __name__ == '__main__':
    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(bi_search(0, len(arr) - 1, sorted(arr), k))