'''
หอคอยแห่งฮานอย
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)
****ห้ามใช้คำสั่ง for, while, do while*****
หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว
คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ
หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html
'''
a = []
b = []
c = []
def pop_and_append(start, dest):
    global a
    global b
    global c
    if start == 'A':
        x = a.pop(0)
    elif start == 'B':
        x = b.pop(0)
    else:
        x = c.pop(0)
    if dest == 'A':
        a.insert(0, x)
    elif dest == 'B':
        b.insert(0, x)
    else:
        c.insert(0, x)
    # print(a, b, c)
def show_tower(maxn, row):
    global a
    global b
    global c
    acp = a[::-1]
    bcp = b[::-1]
    ccp = c[::-1]
    if row == 0:
        return
    if row == maxn:
        print('|  |  |')
    if len(a) >= row:
        print(f"{acp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(b) >= row:
        print(f"{bcp[row-1]}  ", end="")
    else:
        print('|  ', end="")
    if len(c) >= row:
        print(f"{ccp[row-1]}", end="")
    else:
        print('|', end="")
    if row != 0:
        print()
    show_tower(maxn, row-1)
def move(n, start, filler, dest, maxn):
    if n == 1:
        print(f"move {n} from  {start} to {dest}")
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
    else:
        move(n-1, start, dest, filler, maxn)
        print(f"move {n} from  {start} to {dest}")
        pop_and_append(start, dest)
        show_tower(maxn, maxn)
        move(n-1, filler, start, dest, maxn)
def rec_init_a(num, target):
    global a
    if num <= target:
        a.append(num)
        rec_init_a(num+1, target)
_input = int(input("Enter Input : "))
rec_init_a(1, _input)
show_tower(_input, _input)
move(_input, 'A', 'B', 'C', _input)