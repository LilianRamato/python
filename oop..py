#inheritance

class person:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def habari(self):
        print(" hello  my name is"+self.myname)


class student(person):
    def __init__(self,name,age,students_id):
        super().__init__(name,age)
        self.mystudent=students_id
    def habari(self):
        super().habari()
        print("im a student with ID"+str(self.mystudent))

myname=student("joy",18,45934)
myname.habari()
