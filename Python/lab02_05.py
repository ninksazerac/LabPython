#funString
class funString():
    def __init__(self,string =''):
        self.string = string

    def __str__(self):
        return self.string

    def changeSize(self):
        answer = ''
        for i in range(len(self.string)):
            if ord(self.string[i]) >= 65 and ord(self.string[i]) <= 90:
                answer = answer + chr(ord(self.string[i]) + 32)
            elif ord(self.string[i]) >= 97 and ord(self.string[i]) <= 122:
                answer = answer + chr(ord(self.string[i]) - 32)
        return answer

    def size(self):
        return len(self.string)

    def Reverse(self):
        answer = ''
        for i in range(len(self.string)-1,-1,-1):
            answer = answer + self.string[i]
        return answer

    def deleteSame(self):
        answer = ''
        checkDuplicate = []
        for i in range(len(self.string)):
            if self.string[i] not in checkDuplicate:
                answer = answer + self.string[i]
                checkDuplicate.append(self.string[i])
            else:
                continue
        return answer

Inp1, Inp2 = input('Enter String and Number of Function : ').split()
Restring = funString(Inp1)

if Inp2 == '1': print(Restring.size())
elif Inp2 == '2' : print(Restring.changeSize())
elif Inp2 == '3' : print(Restring.Reverse())
elif Inp2 == '4' : print(Restring.deleteSame())