#1
'''จงคำนวณค่า BMI โดยมีสูตรการคำนวณดังนี้

BMI = น้ำหนักหน่วย (kg) / ( ความสูงหน่วย (m) * ความสูงหน่วย (m))

โดยมีเกณฑ์ดังต่อไปนี้

ค่า                             สถานะ

BMI < 18.5               Below normal weight

18.5 <= BMI < 25     Normal weight

25 <= BMI < 30        Overweight

30 <= BMI < 35        Case I Obesity

35 <= BMI < 40        Case II Obesity

BMI >= 40                Case III Obesity



โดยให้แสดงผลลัพธดังตัวอย่าง'''

print(' *** BMI ***')
kg,m=map(str,input('Enter your weight(kg) and height(m) : ').split())
bmi= int(kg) / (float(m) * float(m)) #ได้ค่าbmiทศนิยมเยอะ
if bmi < 18.5 :
    print("Your status is : Below normal weight.")
if 18.5 <= bmi and bmi < 25 :
    print("Your status is : Normal weight.")
if 25 <= bmi and bmi < 30 :
    print("Your status is : Overweight.")
if 30 <= bmi and bmi < 35 :
    print("Your status is : Case I Obesity.")
if 35 <= bmi and bmi < 40 :
    print("Your status is : Case II Obesity.")
if bmi >= 40 :
    print("Your status is : Case III Obesity.")