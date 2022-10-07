fileobj = open("C:/test.txt")

#read whole file
#print(fileobj.read())

#Bring cursor to original position to reread from beginning
fileobj.seek(0)

#place file cursor at position 7
fileobj.seek(7)

#read first 20 characters of the file
fileobj.seek(0)
#print(fileobj.read(20))

# get file cursor point
print(fileobj.tell())

#readline()- reads the line of a file
fileobj.seek(0)
#print(fileobj.readline()) # read 1st line
#print(fileobj.readline()) # read 2nd line


#readlines()- reads all the lines of a file
fileobj.seek(0)
#print(fileobj.readlines())


#read 1st 5 lines of a file using readlines()
'''
fileobj.seek(0)
count = 0
for i in fileobj.readlines():
    if (count<5):
        print(i)
    else:
        break
    count += 1
'''
#write File
fileobj1 = open("C:/test2.txt", 'w')

#add content to existing file
fileobj1.write('This is the new content')
fileobj1.close()

fileobj1 = open('C:/test2.txt', 'r')
print(fileobj1.read())

fileobj1.close()


#delete file
import os
os.remove('C:/test2.txt')
fileobj1 = open('C:/test2.txt', 'r')






















    
