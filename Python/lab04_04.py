#เดาใจไว้แล้วว่าเธอรักฉันแบบที่ฉันรัก
class Queue :
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def enqueue(self, new_data):
        return self.data.append(new_data)

    def dequeue(self):
        if self.is_empty():
            return 'Empty'
        return self.data.pop(0)

    def size(self):
        return len(self.data)

def Activity(num):
    num = int(num)
    if num == 0:
        return 'Eat'
    elif num == 1:
        return 'Game'
    elif num == 2:
        return 'Learn'
    elif num == 3:
        return 'Movie'

def Location(num):
    num = int(num)
    if num == 0:
        return 'Res.'
    elif num == 1:
        return 'ClassR.'
    elif num == 2:
        return 'SuperM.'
    elif num == 3:
        return 'Home'

Mq = Queue()
Yq = Queue()
score = 0
x = input('Enter Input : ').split(',')
for i in x:
    m = ''
    y = ''
    i = i.split()
    Mq.enqueue(i[0])
    Yq.enqueue(i[1])
print('My   Queue = ',end='')
for i in range(0,Mq.size()):
    if i == 0:
        print(Mq.data[i],end='')
    else:
        print(', '+str(Mq.data[i]),end='')
print()
print('Your Queue = ',end='')
for i in range(0,Yq.size()):
    if i == 0:
        print(Yq.data[i],end='')
    else:
        print(', '+str(Yq.data[i]),end='')
print()
print('My   Activity:Location = ',end='')
for i in range(0,Mq.size()):
    list_= []
    list_ = str(Mq.data[i]).split(':')
    if i == 0:
        print(Activity(list_[0])+':'+Location(list_[1]),end='')
    else:
        print(', '+Activity(list_[0])+':'+Location(list_[1]),end='')
print()
print('Your Activity:Location = ',end='')
for i in range(0,Yq.size()):
    list_= []
    list_ = str(Yq.data[i]).split(':')
    if i == 0:
        print(Activity(list_[0])+':'+Location(list_[1]),end='')
    else:
        print(', '+Activity(list_[0])+':'+Location(list_[1]),end='')
print()
for i in range(0,Mq.size()):
    m = Mq.data[i]
    y = Yq.data[i]
    if m[0] == y[0] and m[2] != y[2]:
        score += 1
    elif m[0] != y[0] and m[2] == y[2]:
        score += 2
    elif m[0] == y[0] and m[2] == y[2]:
        score += 4
    else:
        score -= 5
if score > 6:
    print("Yes! You're my love! : Score is "+str(score)+'.')
elif score > 0 :
    print("Umm.. It's complicated relationship! : Score is "+str(score)+'.')
else:
    print("No! We're just friends. : Score is "+str(score)+'.')