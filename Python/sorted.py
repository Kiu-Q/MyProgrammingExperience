# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:37:06 2022

@author: user
"""
fruit=[]
apple=int(input('enter apple cost: '))
fruit.append(apple)
banana=int(input('enter banana cost: '))
fruit.append(banana)
orange=int(input('enter orange cost: '))
fruit.append(orange)
print("you've enter %d cost"%(len(fruit)))
print('the cheapest cost is %d'%min(fruit))
print('the most expensive cost is %d'%(max(fruit)))
print("%d total cost is %d"%(len(fruit),sum(fruit)))
print('the cost in decending order: '+str(sorted(fruit)))
