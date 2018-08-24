

#Q 1)

r = int(input("Enter radius of sphere: "))
pi = 3.14
def getarea(r):
    a=4*pi*r*r
    return a
def getCircumference(r):
    c=2*pi*r
    return c
print("Area of sphere is= ",getarea(r))
print("Circumference is= ",getCircumference(r))


#Q 2)

class student():
      def __init__(self,person_name,person_rno):
          self.name=person_name
          self.rno=person_rno
      def age(self,person_age):
          self.age=person_age
      def marks(self,person_marks):
          self.marks=person_marks
      def display(self):
          print("Name=",self.name,"Roll.o=",self.rno,"Age=",self.age,"Marks=",self.marks)
s=student('Aditya Batra',1046)
s.age(21)
s.marks(78)
s.display()

#Q 3)

class temprature():
    def fahrenheit(self,c):
        self.celcius=c
        self.fahren=(self.celcius*1.8)+32
        print("temp in fahrenheit is:",self.fahren)
    def cel(self,f):
        self.fahren=f
        self.celcius=(self.fahren-32)*1.8
        print("temp in celcius is:",self.celcius)
t=temprature()
t.fahrenheit(32)
t.cel(100)

#Q 4)
class movie_detail():
     def add_detail(self,artist,release,rating):
         self.art=artist
         self.rel=release
         self.rate=rating
     def display(self):
         print(self.art,self.rel,self.rate)
m=movie_detail()
m.add_detail('Amitabh',2012,4)
m.display()

#Q 5)

class Animal():
    def animal_attribute(self,name):
        self.name=name
        print(self.name)
class Tiger(Animal):
    def name(self):
        pass
t=Tiger()
t.animal_attribute("lion")

#Q 6)

#A B
#A B

#Q 7)

class shape():
    def __init__(self,length,breath):
        self.l=length
        self.b=breath
    def area():
        self.ar=self.l*self.b
        print(self.ar)
class rect(shape):
    def area():
        pass         
class square(shape):
    def area():
        pass
s=shape(10,20)
r=rect()
s=square()
r.area()
s.area()
































