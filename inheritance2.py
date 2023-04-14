class Magari:
    def __init__(self,make,model,year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def kuanzisha(self):
        print(f"{self.mymake} {self.mymodel} {self.myyear} started")
class toyota(Magari):
    def __init__(self,make,model,year,num_doors):
        super().__init__(make,model,year)
        self.mynum_door=num_doors

    def kuanzisha(self):
        print(f"{self.mymake}{self.mymodel}car with{self.mynum_door}doors started")
gari=toyota("premio","saloon,2023",2023,5)
gari.kuanzisha()
#create a class of motorcylce with make,model and year,not door but engine size.

class motorcyle:
    def __init__(self,make,model,year):
        self.mymake=make
        self.mymodel=model
        self.myyear=year
    def start(self):
        print(f"{self.mymake}{self.mymodel}{self.myyear} started")
class ducati(motorcyle):
    def __init__(self,make,model,year,engine_size):
        super().__init__(make,model,year)
        self.myengine_size=engine_size
    def start(self):
        print(f"{self.mymake}{self.mymodel}  motorcylce with  {self.myengine_size}engine_size started")

motor=ducati("premium","op3",2023,8600)
motor.start()

class birds:
    def __init__(self,name,type):
        self.bname=name
        self.btype=type
    def describe(self):
        print(f"{self.bname}{self.btype} found")
class flyer(birds):
    def __init__(self,name,type,ability):
        super().__init__(name,type)
        self.bability=ability
    def describe(self):
        print(f"{self.bname} which is {self.btype}  is able to {self.bability}")

birds=flyer("eagle","black_american","see from a far distance")
birds.describe()
