# create a class called shape,with a method called area() that returns 0.# create two subclasses triangle and rectangle ,each childclass should have a method of calculating the area of the shape.
# (for therectangle (length*width) for triangle (base*height1/2)

class Shape:
    def __init__(self, name):
        self.myname = name

    def area(self):
        return 0


class Triangle(Shape):
    def __init__(self, name):
        super().__init__(name)

        self.mybase= float(input("Enter base "))
        self.myheight=float(input("Enter height"))


    def area(self):
       return  print((self.mybase * self.myheight) / 2)


shape = Triangle("Triangle")
shape.area()


class Rectangle(Shape):
    def __init__(self, name):
        super().__init__(name)
        self.mylength=float(input("Enter length"))
        self.mywidth=float(input("Enter Width"))

    def area(self):
     return print((self.mylength * self.mywidth))


rec = Rectangle("Rectangle")
rec.area()

