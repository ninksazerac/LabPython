'''
3 - Exam_3_3_2a
จงเขียนโปรแกรมแบบ Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่ แล้วให้แสดงผลดังตัวอย่าง
'''
def palindrome(str):
    lst=[]
    lstdelete=['?','“','”',';','’','!','.',' ']
    for i in str:
        if i not in lstdelete:
            lst.append(i.lower())
    if len(lst) == 1:  # base case 1st
        return
    elif len(lst) == 2 and lst[0] == lst[-1]:   # base case 2nd
        return
    elif lst[0] == lst[-1]:
        return palindrome(lst[1:-1])  # get only inside of string ... and run it's self again
    else:
        return False    # not a palindrome'''



arr = input('Enter Input : ')
result = palindrome(arr)
if result is False:
    print(f'\'{arr}\'', 'is not palindrome')
else:
    print(f'\'{arr}\'', 'is palindrome')