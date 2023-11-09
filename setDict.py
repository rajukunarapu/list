#set is represented by curly brockets ,unordered and unchangable and dont allow duplicate values

set = {"michael","tom","clark","tom","white",True,1,0,False}
print(set)
#index numbers not work on the set,access through forloop and if
print("tom" in set)
#adding items to set add used to add items and update used to extend items from another set
set.add("chris")
print(set)
set1 = {"roman","cruise","albert"}                         #set methodes
set.update(set1)                                      #add,update,remove,pop,discard,union,difference
print(set)                                     #difference_update(remove the existed items in both set)
#removing items from set
set.remove(True)
print(set)
set.discard(0)
print(set)
set.pop()
print(set)
set3 = set.union(set1)
print(set3)
a = {"apple","mango","orange"}
b = {"red","orange","yellow"}
c = a.difference(b)
print(c)



#dictionaries are ordered,chageable and do not allow duplicate values

dict= { "michael" : "singer" , "white" : "actor" ,"roman" : "wwwE" }
print(dict["michael"])
dict["michael"] = "traveller"        #changing the value of key and add new items to dictionary
print(dict)
dict["anvesh"] = "tourist"           #adding new items to list
print(dict)
y = dict.get("white")                #get the value of the key
print(y)
z = dict.keys()                      #dispaly all the keys in the dictionary
print(z)
x = dict.values()                    #display all the values in the dictionary
print(x)
dict.pop("roman")                    #removing specified key value pair
print(dict)
dict.popitem()                       #removing last item of the dictionary
print(dict)