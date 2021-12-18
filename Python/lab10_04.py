'''
Rehashing

ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
'''

import math


class Hash:
    def __init__(self, table_size, max_collision, threshold=70):
        self.threshold = threshold
        self.max_collision = max_collision
        self.table_size = table_size
        self.element = []   # use this to store inserted element in table instead!
        self.table = []
        for _ in range(table_size):
            self.table.append(None)

    def get_hash(self, key):
        return key % self.table_size

    def number_of_elements(self):
        number = 0
        for i in range(len(self.table)):
            if self.table[i] is not None:
                number += 1
        return number

    def is_full(self):
        return self.number_of_elements() == self.table_size

    def rehash(self, adding=None):
        if adding is not None:
            self.element.append(adding)

        self.table = []

        for possible_prime in range(self.table_size*2, 99999999999999):  # get new prime table size
            for i in range(2, int(math.sqrt(self.table_size*2))+1):
                if possible_prime % i == 0:
                    break
            else:
                self.table_size = possible_prime
                break

        for i in range(self.table_size):
            self.table.append(None)
        for value in self.element:
            retry = 0
            hashed_index = self.get_hash(value)
            while retry < self.max_collision:
                index = (hashed_index + retry ** 2) % self.table_size
                if self.table[index] is None:
                    # print(value, index)
                    self.table[index] = value
                    break
                retry += 1
                print(f'collision number {retry} at {index}')


    def insert(self, value):
        print("Add :", value)

        retry = 0
        hashed_index = self.get_hash(value)
        while retry < self.max_collision:
            index = (hashed_index + retry ** 2) % self.table_size
            if self.table[index] is None:
                if (self.number_of_elements()+1) * 100 / self.table_size > self.threshold:
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehash(value)
                else:
                    self.element.append(value)
                    self.table[index] = value
                return
            retry += 1
            print(f'collision number {retry} at {index}')

        print("****** Max collision - Rehash !!! ******")
        self.rehash(value)

    def __str__(self):
        out = ''
        for i in range(self.table_size):
            out += f"#{i+1}\t{self.table[i]}\n"
        out += '----------------------------------------'
        return out



print(" ***** Rehashing *****")
control, lst = input("Enter Input : ").split('/')
table_size, max_collision, threshold = list(map(int, control.split()))
lst = list(map(int, lst.split()))
print("Initial Table :")
hash = Hash(table_size, max_collision, threshold)
print(hash)
for item in lst:
    hash.insert(item)
    print(hash)