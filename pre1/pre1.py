#Access Modifier
#Public
#Protected _
#Private __
class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self._salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self._salary))
        print("ตำแหน่ง = {}".format(self._department))

obj1 = Employee("toto",20000,"บัญชี")
obj1.name = "yoyo"
obj1._showData()
