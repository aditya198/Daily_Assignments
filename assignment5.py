
#Q 1)
y=int(input("Enter year to check "))
if(y%4==0 and y%100==0 or y%400==0):
    print("Leap year")
else:
    print("Not a leap year")

#Q 2)
l=int(input("enter length"))
b=int(input("enter bredth"))
if(l==b):
    print("These dimensions are of square")

else:
    print("These dimensions are of rectangle")

#Q 3)
a1=int(input("Enter age of 1st person"))
a2=int(input("Enter age of 2nd person"))
a3=int(input("Enter age of 3rd person"))
if(a1<a2 and a3):
    print("a1 is youngest")
elif(a2<a1 and a3):
    print("a2 is youngest")

else:
    print("a3 is youngest")
    
#Q 4)
a=int(input("Enter age"))
choice=input("Enter M for male and F for female ")
if(choice=="F"):
    print("Then she would only work in urban areas")
elif(choice=="M"):
        if(a>20 and a<40):
            print("He may work anywhere")
        if(a>40 and a<60):
            print("He may work anywhere")
        elif(a<20 and a>60):
            print("ERROR")

#Q 5)

units=int(input("enter quantity"))
cost=100*units
print(cost)
if(cost>1000):
    cost=cost-(cost*0.1)
print("Total_cost=",cost)

#Q 6)

a=[]
for i in range(0,10):
    n=int(input(" "))
    a.append(n)
print(a)

#Q 7)

x=0
while(x==0):
    print("zero")

#Q 8)

a=[]
b=[]
n=int(input("Enter total int"))
for i in range(0,n):
    x=int(input(""))
    a.append(x)
    b.append(x*x)
print(a)
print(b)

#Q 9)

x=['chitkara',46,25,20.5]
ints=[]
strings=[]
floats=[]
for i in range(0,4):
    if isinstance(x[i],int):
        ints.append(x[i])
    elif isinstance(x[i],float):
        floats.append(x[i])
    else:
        strings.append(x[i])
print(ints)
print(floats)
print(strings)


#Q 10)

y=[]
for i in range(1,101):
    flag=0
    if i==2:
        y.append(i)
    else:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break;
            else:
                flag=0
        if flag==0:
            y.append(i)
y.remove(1)
print(y)

#Q 11)

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end='')
    print("\r")


#Q 12)

x=[]
for i in range(0,4):
    n=int(input(""))
    x.append(n)
n=int(input("enter no. u want to delete"))
x.remove(n)
print(x)
























































    
























    


                   
