'''
1 - Exam_3_1_2a
จงเขียนโปรแกรมแบบ Recursive เพื่อหาค่าผลรวมตั้งแต่ 1 ถึงเลขที่กำหนด

โดยในโปรแกรมห้ามใช้คำสั่งการวนซ้ำ(while, for) และให้แสดงผลดังตัวอย่าง



สามารถพิมพ์เลขทศนิยมตามจำนวนจุดทศนิยมที่ต้องการได้จากคำสั่ง

print("%.5f" %(3.1428571428))

การใช้งาน
def natural_sum(n):
    #code here

num = int(input("Enter number : "))
print("%.d" %(natural_sum(num)))
'''
def natural_sum(e):
    if e <= 1 :
        return e
    else :
        return e + natural_sum(e-1)

print(" *** Natural sum ***")
num = int(input("Enter number : "))

i = 1
while i <= num :
    print(i,end='')
    i = i+1
    if i <= num :
        print(" + ",end='')
print(" = %.d" %(natural_sum(num)))