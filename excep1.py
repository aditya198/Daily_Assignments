#Q 1)

a=3
if a<4:
    try:
        a=a/(a-3)
        print(a)
    except ZeroDivisionError:
        a=0
        print(a)
#Answer->The error in below statement is 'Runtime error' caused due to "Zero division error" which occurs when a expression is divided by zero.

#Q 2)
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("Index Error")

#Answer->The error occurs because of 'Index Error' as the index of list is out of range. As the list index start from 0 so in print it should be wrtten print(l[2]).

#Q 3)

try:
    raise NameError("Hi there")  
except NameError:
        print("An exception")
        raise

#Answer->It will print 'An exception' first then show error then it will raise
#      ->NameError("Hi there")

#Q 4)

 # Function which returns a/b
 #   def AbyB(a , b):
 #       try:
 #           c = ((a+b) / (a-b))
 #       except ZeroDivisionError:
 #          print("a/b result in 0")
 #      else:
 #         print(c)

# Answer->  AbyB(2.0, 3.0)->
#                           For this function call it would print value of 'c' i.e==>  5.0

#           AbyB(3.0, 3.0)->
#                           a/b result in 0


#Q 5)

#1)Import Error->
#              It is raised when a module or member of module can't be imported.

try:
    from exception import myexception
except Exception as a:
    print(a)
print()

#2)Value Error->
#              If input is not of valid datatype than program raise Value Error.

try:
    n=int(input("Enter number"))
except ValueError:
    print('Error.. numbers only allowed')
else:
    print(n)

#3) Index Error->
#               It is type of error raised when we attempt to access an endex that is outside range of list.
try:
    a=[1,2,3]
    print(a[3])
except IndexError as message:
    print(message)
print()





























    
