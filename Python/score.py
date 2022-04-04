# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 17:03:38 2022

@author: user
"""

chi=input('please type in chinese score: ')
eng=input('please type in english score: ')
mat=input('please type in maths score: ')
sci=input('please type in science score: ')
ave=(int(chi)+int(eng)+int(mat)+int(sci))/4
print('your average score is '+str(ave))