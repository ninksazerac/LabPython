'''
หาค่าที่มากที่สุด
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
ให้เขียน Recursive หาค่า Max ของ Input
'''

def Search(lists,max=None):
    lists = list(lists)
    if len(lists) == 0:
        return max
    elif max == None:
        max = lists.pop()
        return Search(lists,max)
    else:
        temp = lists.pop()
        if temp > max:
            max = temp
        return Search(lists,max)

inp = list(map(int, input('Enter Input : ').split()))
print('Max :',Search(inp))