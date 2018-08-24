#Q 1)

n = int(input("Enter number of items you want to enter: "))
d ={}
for i in range(n):
    text = input("Enter key:value = ").split(":")
    d[text[0]] = text[1]
print(d)

#Q 2)

n = int(input("Enter the number of keys you want: "))
d = {}
for i in range(0,n):
    a = input("Enter student name: ")
    d[a] = {}
    b = int(input("Marks in Physics: "))
    d[a]['Physics'] = b
    c = int(input("Marks in Chemistry: "))
    d[a]['Chemistry'] = c
    e = int(input("Marks in Maths: "))
    d[a]['Maths'] = e
name = input("Enter name of the student whose result you want to find: ")
for i in d:
    if(name==i):
        print(i,d[i])

