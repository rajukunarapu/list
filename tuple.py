#tuple are ordered,unchangable and allowduplicate values
x = ("michael","tom","tom","storm","white",33,True,True,)
print(x)
print(x[-1])
print(x[2: ])
#tuple items are unchangable ,tuple convert into list and make changes and convert into tuple
a = list(x)
a[-1]="mike"
a[-2]="albert"
x = tuple(a)
print(x)
#adding items to tuple , tuple coonvert into list
b = list(x)
b.insert(4,"roman")
b.append(22)
b.remove(33)
b.pop(-1)
b.sort()
x = tuple(b)
print(x)
c = list(x)
c.reverse()
x = tuple(c)
print(c)
#normally,storing items into the variables is called "packing" and unpacking is called as extract the values to the vaiables
fruits = ("mango","orange","apple")
(yellow,red,black) = fruits
print(yellow)
print(red)
print(black)
#join the two tuple
print(x+fruits)
