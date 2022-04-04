# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:11:52 2022

@author: user
"""

f=open('file.txt','r')
print('word in file: ')
for line in f:
    print(line)
f.close()
enter=input('write or append: ')
if (enter=='write'):
    f=open('file.txt','w')
    enter=input('enter word write in: ')
    f.write(enter)
    f.close()
elif(enter=='append'):
    f=open('file.txt','a')
    enter=('\n'+input('enter word append in: '))
    f.write(enter)
    f.close()
else:
    print('invoid enter')