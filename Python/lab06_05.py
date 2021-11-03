'''
วาดภาพแสนสุข
เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว
'''
up=1
down=0
def staircase(n):
    global up,down
    s1 = '___________________________________________________'
    s2 = '###################################################'
    if n > 0:
        print(f'{s1[:n-1]}{s2[:up]}')
        up += 1
        if n != 1:
            staircase(n - 1)
    elif n < 0:
        print(f"{s1[:down]}{s2[:n*-1]}")
        down += 1
        if n != -1:
            staircase(n + 1)
    else:
        print("Not Draw!")

staircase(int(input("Enter Input : ")))