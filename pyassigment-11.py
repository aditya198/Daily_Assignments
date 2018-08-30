# Q 1)


import re 
n=input("Enter Email-id")
c=0
m=re.finditer('[a-zA-Z][a-zA-Z0-9_.]*[@](gmail.com|yahoo.com|hotmail.com|outlook.com)',n)
for i in m:
    c=c+1
    print('{} is a valid email-id'.format(i.group()))
if(c==0):
          print("Not a valid email-id")

          

# Q 2)

import re 
n=input("Enter Phone number")
count=0;
a=re.finditer('[6-9][0-9]{9}',n)
for i in a:
    count=count+1
    print('{} is a valid Phone number'.format(i.group()))
if(count==0):
    print("It is not a valid Phone number")
    
