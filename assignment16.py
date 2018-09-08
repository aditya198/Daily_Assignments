
#Q-1)

import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student_collection']

#Q-2)

for i in range(10):
    try:
        name=input("Enter name: ") 
        marks=int(input('Enter  Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
    except ValueError as msg:
        print(msg)
        
#Q-3)
        
for i in range(10):
    try:
        name=input("Enter name: ") 
        marks  int(input('Enter  Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry')
            i=i-1
        else:
            collection.insert_one({'Name':name,'Marks':marks})  
            i=i+1
    except ValueError as msg:
        print(msg)

#Q4)
        
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)
