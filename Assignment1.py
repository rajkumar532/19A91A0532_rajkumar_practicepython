'''
1. Write a Python Program to read the contents of a file and count the size of file
   then count how many times "CSE" is existed in the file.
'''
import os
file1 = open('SampleCSE.txt','r')
data = file1.read()
print('Details of the File is')
print(data)
size = os.path.getsize('SampleCSE.txt')
print('Size of the file is',size,'bytes')
count = data.count('CSE')
print('Number of occurences of CSE existed in the file is',count)
file1.close()
'''
Output:
Details of the File is
I have chosen Computer Science and Engineering (CSE) in
my academic year of 2019-2023 because, I love to enjoy playing
with computers and learn depth about it. So that is why I have
chosen CSE branch and motivate others to join in this CSE branch
other than any other branches.
Size of the file is 281 bytes
Number of occurences of CSE existed in the file is 3
'''
