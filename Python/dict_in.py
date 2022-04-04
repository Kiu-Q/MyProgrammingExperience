# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:13:14 2022

@author: user
"""

people=dict(thomas=13, sofia=10, siufa=6)
enter=input('age enter or check: ')
age=0
if enter in people:
    print(enter+"'s age is "+str(people[enter]))
else:
    age=input('enter age: ')
    people[enter]=age
    print(enter+"'s age is "+str(people[enter]))