# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:04:02 2022

@author: user
"""

cost=dict(apple=2, banana=3, orange=3)
enter=input('enter fruit: ')
if(enter=='apple'or enter=='banana' or enter=='orange'):
    print(enter+'cost is $'+str(cost[enter]))
else:
    print('please try again')