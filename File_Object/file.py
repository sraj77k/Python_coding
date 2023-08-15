#1. Read mode
"""f = open('name.txt','r')
print(f.name)
print(f.mode)
f.close()"""

#2.

with open('name.txt', 'r') as f:
    #print(f.read())
    #f_contents = f.read()
    f_contents = f.readline()
    #f_contents = f.readlines()
    print(f_contents, end ='')

f.close()