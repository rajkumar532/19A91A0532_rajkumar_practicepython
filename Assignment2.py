'''
2. Write a Python Program to read the contents of a file and find how many upper case letters,
   lower case letters and digits existed in the file.
'''
file = open('SampleCount.txt','r')
data = file.read()
print('Contents of a file is')
print(data)
digit = upper = lower = special = 0
for ch in data:
    if ch.islower():
        lower += 1
    elif ch.isupper():
        upper += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print('Number of Upper Case Letters in a file is',upper)
print('Number of Lower Case Letters in a file is',lower)
print('Number of digits in a file is',digit)
print('Number of Special Characters in a file is',special)
file.close()
