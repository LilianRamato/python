#class is a collection  or instance of an object
#def_init_(self is a keyword ...def is a function
class fruits:
    def __init__(self,type,colour,price):
        self.mytype=type
        self.mycolour=colour
        self.myprice=price
    def onyesha(self):
        print(self.mytype,self.mycolour,self.myprice)

#create an object:this is a blueprint of a class

myobj=fruits("banana","yellow",20)
myobj.onyesha()
myobj1=fruits("pineapple","yellow",30)
myobj1.onyesha()
myfav=fruits("mango","redorange",50)
myfav.onyesha()
myfav1=fruits("apple","green",25)
myfav.onyesha()


class salary:
    def __init__(self,name,id,amount):
        self.employeename=name
        self.employeeid=id
        self.employeeamount=amount
    def showresults(self):
        print(self.employeename,self.employeeid,self.employeeamount)

results=salary("joy","010101",30000)
results.showresults()
results1=salary("ian","020202",12200)
results1.showresults()
results2=salary("gift","939495",40500)
results2.showresults()






















