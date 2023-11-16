#Functons
def my_class(age):
    print("the person eligible for vote is {}".format(age))
my_class(19)

# * used to pass number of arguments and accessed through tuple indexing
def my_class(*name):
    print("the person name is "+name[1])
my_class("john","jacob","michael")

# ** used to pass number of elements and accessed through dictonary
def my_function(**country):
    print("the name of country is "+country["ind"])
my_function(ind = "india", aus =" austraila", us = "united states")

def my_function1(child3,child1,child2):
    print("his name is "+child3)
my_function1("mike","bob","alice")
