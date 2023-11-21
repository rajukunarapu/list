# Polymorphism means mutiple methods with same name
#1.overloading:- same method with different parameters
#2.overriding:- same method with same parmeters

class car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move function in car class")
class bike():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move function in bike class")
class truck():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move function in truck class")
car11 = car("tata","rangrover")
bike11 = bike("ktm","duke")
truck11 = truck("ashokleyland","123")
for x in (car11,bike11,truck11):               # using for loop
    x.move()
print(" ")                                  # spacce between these two
car11.move()                                 # using seperate function call
bike11.move()
truck11.move()

class car2():
    def __init__(self,brand1,color1):
        self.brand1 = brand1
        self.color1 = color1
    def function1(self):
        print("funcion1 in car2 class")
class bike2(car2):
    def function1(self):
        print("funnction1 in bike class")
class truck2(car2):
    def function1(self):
        print("function1 in truck1 class")
print(" ")
car22 = car2("lamborgini","blue")
bike22 = bike2("ns200","black")
truck22 = truck2("volvo","white")
for i in (car22,bike22,truck22):
    print(i.brand1)
    print(i.color1)
    i.function1()