
#Q 1)

 
import datetime         # import datetime module
import datetime as dt   #renaming datetime as dt
o=dt.datetime.now()     #storing current time in variable
print(o)


#Q 2)

import webbrowser                                                               #import webbrowser module
youtube=input('Enter which video to play')                                      #Taking input from user for topic of which video to play
webbrowser.open_new_tab("http://www.youtube.com/search?btnG=1&q=%s" % youtube)  #Helps to open new tab containg videos of our searched topic

#Q 3)

import os,sys
d=os.listdir(directory1)            #Making list of files in directory
for file in diretory:               #Accessing all files in directory
   os.rename('file.txt','file.jpg') #Renaming all files in directory

