#5
'''
จงสร้าง class MyInt ซึ่งคลาสนี้เป็นคลาสที่เก็บเลขจำนวนเต็มโดยมี method ดังต่อไปนี้

__init__ สำหรับสร้างคลาส โดยรับจำนวนเต็มเพื่อใช้เป็นตัวแปรในคลาส

isPrime สำหรับตรวจสอบว่าตัวเลขนั้นเป็นจำนวนเฉพาะหรือไม่

showPrime สำหรับแสดงเลขจำนวนเฉพาะระหว่าง 2 ถึงเลขนั้น

__sub__ สำหรับลบค่าตัวตั้งด้วยค่าครึ่งหนึ่งของตัวลบ



โดยมีการเรียกใช้งานดังนี้



a = MyInt(20)

b = MyInt(17)

print(a.isPrime())

print(b.isPrime())

print(a.showPrime())

print(b.showPrime())

print(a-b)



ผลลัพธ์

False

True

2 3 5 7 11 13 17 19

2 3 5 7 11 13 17

12


โดยให้เขียนโปรแกรมเพื่อรับค่า ตัวเลข 2 ตัว และแสดงผลดังตัวอย่าง
'''

class myint:
    def __init__(self, default):    #สำหรับสร้างคลาส โดยรับจำนวนเต็มเพื่อใช้เป็นตัวแปรในคลาส
        self.value = default

    def isPrime(self):  #สำหรับตรวจสอบว่าตัวเลขนั้นเป็นจำนวนเฉพาะหรือไม่
        if self.value == 2:
            return f'{self.value} isPrime : True'
        if self.value <= 1:
            return f'{self.value} isPrime : False'
        for i in range(2, 1 + self.value // 2):
            if self.value % i == 0:
                return f'{self.value} isPrime : False'
        return f'{self.value} isPrime : True'

    def showPrime(self):    #สำหรับแสดงเลขจำนวนเฉพาะระหว่าง 2 ถึงเลขนั้น
        if self.value <= 1:
            return '!!!A prime number is a natural number greater than 1'

        def check_prime(v):
            if self.value == 1:
                return False

            if self.value == 2:
                return True

            for x in range(2, 1+v//2):
                if v % x == 0:
                    return False
            return True
        out = ''
        for i in range(2, 1+self.value):
            if check_prime(i):
                out += str(i)+" "
        return out

    def __sub__(self, minus):   # สำหรับลบค่าตัวตั้งด้วยค่าครึ่งหนึ่งของตัวลบ
        return self.value - (minus.value // 2)


def use(in1, in2):
    a = myint(in1)
    b = myint(in2)
    print(a.isPrime())
    print(b.isPrime())
    print(f'Prime number between 2 and {a.value} : ' + a.showPrime())
    print(f'Prime number between 2 and {b.value} : ' + b.showPrime())
    print(f"{a.value} - {b.value} = {a - b}")


'''/////////////////////////////////////////////////////////////////////////////'''
print(' *** class MyInt ***')
numberin = list(map(int, input('Enter 2 number : ').split()))
use(numberin[0], numberin[1])


