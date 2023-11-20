# Inheritance
# chilld class(derived class) inherits methodes,properties from the parent class(base class)

class class1():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printmethod(self):
        print("my name is "+self.name)
class class2(class1):
    pass

obj = class2("john",21)       # it inherits the methods from the parent class
obj.printmethod()


class parent():
    def __init__(self,name1,age1):
        self.name1 = name1
        self.age1 = age1
    def method(self):
        print(self.name1,self.age1)
class child(parent):
    def __init__(self,name1,age1):
        parent.__init__(self,name1,age1)
        self.branch = "cse"                         # adding a new item to function
obj1 = child("michael",21)
obj1.method()
print(obj1.branch)

class baseclass():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def function1(self):
        print(self.fname,self.lname)
class derivedclass(baseclass):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year = year
object1 = derivedclass("roman","reings",25)
object1.function1()
print(object1.year)