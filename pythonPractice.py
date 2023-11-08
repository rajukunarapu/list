# lists are ordered, changeable and allowduplicate items
list = ["michael","michael","bob"]
print(list[0])
print(list[-1])
print(list[2: ])
print(list[ :-1])
list.append("white")
print(list)
list1 = ["stephen","robot",]
list.extend(list1)
print(list)
list.remove("bob")
print(list)
list.pop(-1)
print(list)
list[1] = "markov"
print(list)
list.insert(4,"james")
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.sort(reverse = True)
print(list)
print(len(list))

# tuples are ordered,unnchangeable and allow duplicate items
tuple1 = ("muscow","italy","brazil")
print(tuple1[0])
print(tuple1[-1])
print(tuple1[ :-1])
(japan,china,nepal) = tuple1
print(japan)
print(china)
print(nepal)

# sets are unnordered , unchangeable and donot allow duplicate items
set = {"india","austraila","newzyland"}
print("india" in set)
#set items unchangeable ,but can add and remove the items
set.remove("india")
print(set)
set.add("bharath")
print(set)
set.discard("austraila")
print(set)
set1 = {"afriaca","ameriaca","iran","bharath"}
set.update(set1)
print(set)
z = set.union(set1)
print(z)
set.difference(set1)
print(set)
set.difference_update(set1)
print(set)

# dictionaries are ordered , changeable and donot allow duplicate items
dict = {"asia" : "bharath","europe" : "italy" , "africa" : "egypt"}
print(dict["asia"])
print(dict.get("afriaca"))
dict["color"] = "red"
print(dict)
dict1 = {"class":"nobody","anvesh":"tourist"}
dict.update(dict1)
print(dict)
dict.pop("class")
print(dict)
dict.popitem()
print(dict)
x = dict.keys()
print(x)
y = dict.values()
print(y)