
#If else loop
marks = int(input("marks: "))
if marks>75:
    print("first class with distinction")
elif marks>55:
    print("second class with distinction")
else:
    print("pass")


#For loop
for i in range(8):
    print(i)

for i in range(0,8):
    i+=2                      # increment 0 to 2 next increment count is 1 by default = 0+2 , 2+1 , 3+1
    print(i)
    if i==5:
        break

for i in range(0,10,2):
    i+=1
    if i==5:
        continue
    print(i)

#while loop
a = 0
while a<10:
    a+=2
    print(a)

b = 0
while b<20:
    b+=3
    print(b)
    if b == 9:
        break

    