#3
'''
ให้เขียนโปรแกรมเพื่อหาข้อมูลที่มีความถี่มากกว่าครึ่งหนึ่งของจำนวนข้อมูลทั้งหมดที่รับเข้ามา โดยอ่านค่าจำนวนเต็มจนกระทั่งพบ -1

การแสดงผล

แสดงข้อมูลที่มีความถี่มากกว่าครึ่งหน่ึงของข้อมูลท้ังหมด (ไม่รวม -1)
ถ้าไม่มีข้อมูลที่มีความถี่มากกว่าครึ่งหน่ึงเลย ให้แสดง Not found
ถ้าข้อมูลที่ป้อนเข้ามาไม่มี -1 ให้แสดงผล Invalid INPUT !!!
ข้อมูลที่มีความถี่ครึ่งนึง จะแสดงผล Not found
'''
number1=input('Enter number end with (-1) : ').split()
listt = []
c = 0  # counter
num = 0
p = 0  # nopass

if not '-1' in number1:
    print('Invalid INPUT !!!')

else:

    for i in number1:
        if (i != '-1'):
            listt.append(i)
        else:
            break

    for k in range(len(listt)):
        x = listt.count(listt[k])
        if x > len(listt) / 2:
            if x == c and num != listt[k]:
                c == 0
            elif x > c:
                c = x
                num = listt[k]
    if c == 0:
        print('Not found')
    else:
        print(num)
