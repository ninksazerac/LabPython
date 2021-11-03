'''
POWER!

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab
'''
def power(base,exalt,out = None):
    if exalt == 0:
        return 1
    elif exalt == 1 and out is not None:
        return out*base
    elif out == None:
        out = base
        return power(base,exalt-1,out)
    else:
        return power(base,exalt-1,out*base)

num = list(map(int, input('Enter Input a b : ').split()))
num=power(num[0],num[1])
print(num)
