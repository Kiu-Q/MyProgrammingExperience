# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:54:18 2022

@author: user
"""

password='Ltk20080607'
for i in range(1,11):
    enter=input('Enter password: ')
    if(enter==password):
        print('password correct')
        break
    else:
        print('please try again')
if(enter==password):
    print('you are logged in')
else:
    print('your password was wrong for 10 times, ')
    print('please try again later')