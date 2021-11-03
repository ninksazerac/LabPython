'''
Reverse Sort List
จงเขียนฟังก์ชั่นสำหรับการเรียงค่าใน List ของจำนวนเต็มโดยจะเรียงค่าจากมากไปน้อย
****ห้ามใช้ for/while และฟังก์ชั่นอื่นๆในการวนลูป ให้ใช้ recursion ในการเขียนเท่านั้น****
'''

def searchmax(lst,max=None):
    lst = list(lst)
    if len(lst) == 0 :
        return max
    elif max == None:
        max = lst.pop()
        return searchmax(lst, max)
    else:
        num = lst.pop()
        if num > max:
            max=num
        return searchmax(lst,max)

def sort(inp,out,leng):
    if len(out) < leng:
        num = searchmax(inp)
        out.append(num)
        inp.remove(num)
        if len(out) == leng:
            return out
        else:
            return sort(inp,out,leng)
    else:
        return out

lst = list(map(int, input('Enter your List : ').split(',')))
lst=sort(lst,[],len(lst))
print(f"List after Sorted : {lst}")
