from math import pi


class Spherical:
    def __init__(self, r):
        self.radius = r

    def changeR(self, Radius):
        self.radius = Radius

    def findVolume(self):
        return 4 / 3 * pi * (self.radius * self.radius * self.radius)

    def findArea(self):
        return 4 * pi * self.radius * self.radius

    def __str__(self):
        return 'Radius =' + str(self.radius) + ' Volumn = ' + str(self.findVolume()) + ' Area = ' + str(self.findArea())


Inp1, Inp2 = input('Enter R : ').split()
R1 = Spherical(int(Inp1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(Inp2))
print(R1)