'''
จองรถตู้
บริษัทแห่งหนึ่งมีรถตู้ K คันที่ลูกค้าสามารถเช่าไปใช้งานได้ โดยรถตู้แต่ละคันมีรหัสประจำตัวรถเป็นหมายเลขจำนวนเต็มบวกตั้งแต่ 1 จนถึง K ข้อกำหนดในการเลือกรถตู้ให้ลูกค้ามีอยู่ว่า ลูกค้าจะต้องทำการจองรถตู้ก่อน โดยคำสั่งจองจะต้องระบุจำนวนวันที่จะใช้ จากนั้นผู้จองจะได้รถตู้ที่ว่างให้ใช้เร็วที่สุดเท่าที่จะหาได้จากรถตู้ทั้งหมด

ในกรณีที่มีรถตู้ว่างให้ใช้เร็วที่สุดมากกว่า 1 คัน คันที่มีรหัสประจำรถน้อยกว่าจะถูกเลือกก่อน เช่นถ้าหากมีรถตู้ที่ว่างให้ใช้เร็วที่สุด 3 คัน  ซึ่งมีรหัสประจำรถเป็น 5 , 7 และ 20 รถตู้ที่มีหมายเลข 5 จะถูกเลือกก่อน นอกจากนี้การจองจะให้ความสำคัญกับคำสั่งจองที่มาก่อนเสมอ สำหรับการจองแต่ละครั้ง ผู้จองจะได้รับคำตอบกลับมาว่าได้ใช้รถตู้หมายเลขใด  โดยในตอนแรกรถตู้ทุกคันจะว่างและพร้อมใช้งานทั้งหมด

อธิบาย Input โดย Input จะแบ่งเป็น 2 ฝั่งด้วย /
-  ฝั่งซ้ายเป็น K ซึ่งหมายถึงเลขประจำตัวรถ โดยเริ่มตั้งแต่ 1 ถึง K
-  ฝั่งขวาเป็น List จำนวนวันที่จองรถตู้ของลูกค้าที่สั่งจองเข้ามา

คำใบ้ :  Min Heap
'''
def printTree(n, level=0):
    if n > len(num)-1:
        return
    printTree(2 * n + 2, level + 1)
    print('        ' * level, num[n])
    printTree(2 * n + 1, level + 1)


k, dayList = input('Enter Input : ').split('/')
dayList = [int(i) for i in dayList.split()]

num = []
van = {}    # dict

for i in range(int(k)):
    num.append(i + 1)           # number of van
    van[i+1] = van.get(i+1, 0)  # set day to 0 of van  // .get(data, defaultNum)

for i in range(len(dayList)):
    #printTree(0)

    minNum = num.pop(0)
    van[minNum] = van.get(minNum, 0) + int(dayList[i])    # add day reserve by dayList[i]
    print(f'Customer {i+1} Booking Van {minNum} | {dayList[i]} day(s)')
    #print('--------------------------------------------------')

    for index in range(len(num)):   # run every index

        # day[0] < day[1,2,3,4,5,6,7,8...] // day[0] == day[1,2,3,4,5,6,7,8...] and minNum < number (same day..different number)
        if van[minNum] < van[num[index]] or (van[minNum] == van[num[index]] and minNum < num[index]):
            num.insert(index, minNum)  # sorted and insert min between list
            minNum = None
            break

    if minNum is not None:  # if can't insert and have minNum
        num.append(minNum)  # append last one to num