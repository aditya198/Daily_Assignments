
#Q1 )

li=[1,2,3,4]
li_sq=[i**2 for i in li]
print(li_sq)

#Q2 )

x=int(input("Enter the range: "))
li=[i for i in range(1,x) if all(i%y!=0 for y in range(2,i))]
print(li)

#Q.3 )

#A List Comprehension is like the plain range function, executes immediately and returns a list.
#A Generator Expression returns and object that can be iterated over.
#The comparision is not perfect because in an object returned by the generator expression we cannot access an element by index.
#The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets [] while the Generator expression is enclosed in plain parentheses ()

#Q.4 )

Celsius=[39.2, 36.5, 37.3, 37.8]
far=list(map(lambda x:(x*1.8)+32,Celsius))
print(far)

#Q.5 )

li=[5,12,15,3,13]
li_sq=list(map(lambda i: i*i,li))
print(li_sq)

#Q.6 )

def isprime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
        else:
            return True
li=[15,26,33,13,53,97,22]
a = list(filter(isprime, li))
print(a)

#Q.7 )

li=[5,50,15,20]
from functools import *
x=reduce(lambda x,y:x*y,li)
print(x)








