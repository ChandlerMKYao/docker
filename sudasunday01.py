#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:11:08 2018

@author: mingkangyao
"""

#problem2
c = 50.0
a = 30.0
b = (pow(c,2)-pow(a,2))**0.5
print(b)
#problem3
a1 = 2.5
b1 = 7 
c1 = 6
print(a1/b1)
print(b1%c1)
print(c1/a1)
print(pow(b1,3))
#problem4
from fractions import Fraction
Fraction(3+3/5).limit_denominator()
Fraction(pow(3/7,2)).limit_denominator()
Fraction(1/8*(-2/9)+7/8).limit_denominator()
Fraction('11/13')
Fraction('1.25').limit_denominator()
#problem5
d = '0123456789'
d[::2]
d[1:4]
d[1::2]
d[::-1]
d[-2::-2]
#problem6
e = 'You need Python'
print(e[0],e[-1])
print(len(e))
e = 'I'+e[3:]
print(e)
print(e.title())
print(e.replace(' ','@'))
newe=e.replace(' ','@')
print(newe[::-1])
#problem7
list7=['010','021','0512','0571']
print(list7)
#problem8
list8=[1,2,3,4,5]
for i in list8:
    if i%2==0:
        list8.remove(i)
    i=i+1
print(list8)
#problem9
list9=[[1,2],"python",234,3.14]
list9_1=list9[0]
print(list9_1[0])
list9_2=list9[1]
print(list9_2[-1])
list9_3=list9[2:4]
print(list9_3)
print(list9[-1])
#problem11
a11 = 'noon'
a11re = a11[::-1]
count = 0
for i in range(len(a11)):
    if a11[i]!=a11re[i]:
        print('false')
        break
    count=count+1
if(count==len(a11)):
    print('True')
