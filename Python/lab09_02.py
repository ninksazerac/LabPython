'''
เรียงลำดับโดยไม่สนจำนวนเต็มลบ

ให้เรียงลำดับ input จากน้อยไปมากของจำนวนเต็มบวกและศูนย์ โดยถ้าหากเป็นจำนวนเต็มลบไม่ต้องยุ่งกับมัน
****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง
'''
def sort_dontcare(lst):
    to_sort = []
    minus = []
    for i in range(len(lst)):
        if lst[i] >= 0:
            to_sort.append(lst[i])
        else:
            minus.append((i, lst[i]))
    # print(to_sort, minus)
    for i in range(len(to_sort)-1):
        swapped = False
        for j in range(len(to_sort)-1-i):
            if to_sort[j] > to_sort[j+1]:
                to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]
                swapped = True
        if not swapped:
            break
    for pair in minus:
        to_sort.insert(pair[0], pair[1])
    for item in to_sort:
        print(f'{item} ', end="")


in_lst = list(map(int, input("Enter Input : ").split()))
sort_dontcare(in_lst)