#4
'''จงเขียนโปรแกรมรับเลขจำนวนเต็มบวก 1 จำนวน แล้วแสดงผลตามตัวอย่าง

(หากเลขที่ป้อนเข้าไปอยู่ นอกเหนือช่วง 1-15 ให้แสดงข้อความแจ้งดังตัวอย่าง) A=10 B=11 C=12 D= 13 E=14 F=15

หมายเหตุ

การแสดงผลเลขฐาน 16 สามารถใช้คำสั่งนี้

print("%X" %(12))'''
number=int(input("Enter a positive number : "))
numbers= '123456789ABCDEF'
list1=[]
list2=[]
if 0 < number < 16:
    for x in range(1,number+1):
        if x < 10:
            list1.append(str(x))
        else:
            list1.append(numbers[x-1])
    for x in reversed(list1):
        list2.append(x)


    print(*list1, sep=" ")
    for x in range(number-2):
        y = str(list1[x+1])
        for _ in range(number*2-3):
            y+= ' '
        y+=str(list1[x])
        print(y)
    if number!=1:
        print(*list2, sep=" ")

elif number <= 0:
    print('%d is too low.'%number)
elif number >= 16:
    print('%d is too high.'%number)

'''bug input : 4'''

