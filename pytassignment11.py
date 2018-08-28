#Q 1)

n=int(input("Enter number: "))
f=open('python.txt','r')
for i in range(0,n):
    data=f.readline()
    print(data)
f.close()

#Q 2)

f=open('python.txt','r')
a=f.read()
n=input("Enter the value to be counted: ")
b=a.count(n)
print("{} occurs {}".format(n,b))

#Q 3)

a=open('python.txt')
c=open('assg.txt','a')
b=a.read()
c.writelines(b)
c.close()
a.close()

#Q 4)

x=open('python.txt','r')
y=open('assg.txt','r')
z=open('out.txt','w+')
a=x.readlines()
b=y.readlines()
for i,j in zip(a,b):
    z.write(i)
    z.write(j)
l=z.read()
print(l)
z.close()
y.close()
x.close()

#Q 5)

f=open('python.txt')
d=open('assg.txt','w+')
a=f.readlines()
a.sort()
d.write(str(a))
d.seek(0)
b=d.read()
print(b)
