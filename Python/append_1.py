# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 08:30:33 2022

@author: user
"""

score=[]
enter=0
print('type in score, -1 to quit')
while(enter!= -1):
    enter=int(input('type in score'))
    score.append(enter)
average=sum(score)/(len(score)-1)
score.pop(len(score)-1)
print('all the score: '+str(score))
print('average is: '+str(average))