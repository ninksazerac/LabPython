'''
Find the Running Median
เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง
***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***
***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี
- bubble sort
- straight selection sort
- insertion sort
- shell sort
- merge sort
- quick sort
- minHeap and maxHeap
พิมพ์คำตอบลงในช่อง Ans = "xxx"
***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***
'''
def selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i+1, len(n)):
            if n[min_index] > n[j]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n



l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "minHeap and maxHeap"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    lst = []
    for i in l:
        lst.append(i)
        lst_sorted = selection_sort(lst.copy())
        if len(lst_sorted) <= 1:
            print(f"list = {lst} : median = {lst_sorted[0]:.1f}")
        else:
            print(f"list = {lst} : median = {lst_sorted[len(lst)//2] if len(lst)%2==1 else (lst_sorted[len(lst)//2-1]+lst_sorted[len(lst)//2])/2:.1f}")