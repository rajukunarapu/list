# class keyword used to create the class, It is a blueprint of an object
# objectname = classname(arguments) , It is an real world entity

class csm:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("His name is "+self.name+" he got the "+self.marks+" marks")
    def person(self,htno,branch):
        self.htno = htno
        self.branch = branch
        print("His hallticket number is "+self.htno)
        return self.branch
obj = csm("mike","75")
print(obj.person("101","computer science"))

def my_function(a=10,b=20):
    print("This is the addition operation")
    return a+b
print(my_function(20,20))
print(my_function())

def my_class(*n):                                # Access like tuple
    print("My friend name is "+n[2])
my_class("raju","ramu","raghu","rahul")


def my_class1(**m):                              # Access like dictionary
    print("icc men's world cup won by"+m["ind"])
my_class1(aus ="austraila" , ind = "india", us = "united states")

def my_fav(num):
    return lambda num: num+num
x = my_fav(10)
print(x(20))

class class1():
    def __init__(self,name1,age1):
        self.name1 = name1
        self.age1 = age1
        print("people call him as "+self.name1)
    def function1(self,country,place):
        self.country = country
        self.place = place
        print("His from "+self.country)
obj1 = class1("Ghost",19)
obj1.function1("Euroupe","France")
print(obj1.country)
print(obj1.place)
print(obj1.name1)
print(obj1.age1)

class class2():
    def __init__(self,name2,age2):
        self.name2 = name2
        self.age2 = age2
    def __str__(self):
        return f"{self.name2} age is {self.age2}"
obj2 = class2("john",20)
print(obj2)


class class3():
    def __init__(self,name3,country3):
        self.name3 = name3
        self.country3 = country3
    def fav(self):
        print("This person name is "+self.name3+" his from "+self.country3)
obj3 = class3("michael","india")
obj3.fav()