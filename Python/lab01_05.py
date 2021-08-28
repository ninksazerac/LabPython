print('*** Fun with countdown ***')
a = map(int,input('Enter List : ').split())
list = []
answer1 = []
answer2 = []
count = 0
current = 0
countdown = False

for i in a:
    list.append(i)

for x in range(len(list)):
    if(list[x] == 1):
        answer1.append(list[x])
        answer2.append(answer1.copy())
        answer1.clear()
        count = count + 1
    elif(x != len(list)-1):
        if(list[x] - list[x+1] == 1):
            if(list[x] != 1):
                answer1.append(list[x])
            else:
                answer1.append(list[x])
                count = count + 1
print([count,answer2])
