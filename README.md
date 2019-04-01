# docker
test and explore
###file edit
f=open('/Users/mingkangyao/Desktop/testtxt.txt')
boy=[]
girl=[]
count=1
for each_line in f:
    if each_line[:6]!='######':
        (role,line_spoken)=each_line.split(':',1)
        if role=='A':
            boy.append(line_spoken)
        else:
            girl.append(line_spoken)
    else:
        file_name_boy='boy_'+str(count)+'.txt'
        file_name_girl='girl_'+str(count)+'.txt'
        boy_file=open(file_name_boy,'w')
        girl_file=open(file_name_girl,'w')
        boy_file.writelines(boy)
        girl_file.writelines(girl)
        boy_file.close()
        girl_file.close()
        boy=[]
        girl=[]
        count+=1
f.close()
###Hanoi
def hanoi(n,x,y,z):
    if n==1:
        print(x,"->",z)
    else:
        hanoi(n-1,x,z,y)
        print(x,"->",z)
        hanoi(n-1,y,x,z)
hanoi(5,"x","y","z")
###guess number
import random
i=1
ans=random.randint(1,100)
guess=0
while guess!=ans:
    temp=input("a number:")
    guess=int(temp)
    if guess==ans:
        print("right")
        break
    else:
        if guess>ans:
            print("too large")
            i=i+1
        else:
            print("too small")
            i=i+1
    if i>5:
        print("end")
        break
print(ans)
import easygui as g
import sys
while 1:
    g.msgbox('start')
    msg='who are you'
    title='answer'
    choices=['doctor','master','bachelor','high school']
    choice = g.choicebox(msg,title,choices)
    g.msgbox('I am:'+str(choice),'result')
    msg='restart'
    title='choice'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
###clock
import time as t
class MyTimer():
    def __init__(self):
        self.unit=['year','month','day','hour','minute','second']
        self.prompt='not start'
        self.last=[]
        self.begin=0
        self.end=0
    def __str__(self):
        return self.prompt
    __repr__=__str__
    def start(self):
        self.begin=t.localtime()
        print('clock start')
    def stop(self):
        self.end=t.localtime()
        self._calc()
        print('clock stop')
    def _calc(self):
        self.last=[]
        self.prompt='total time is '
        for index in range(6):
            self.last.append(self.end[index]-self.begin[index])
            self.prompt +=(str(self.last[index])+self.unit[index])
t1=MyTimer()
#连块除法
a=input()
a=[float(i) for i in a.split()]
def Specialdiv(x):
    n=len(x)
    s=float(x[n-1])
    for i in range(n-1,0,-1):
        s=1.0/s
        s=x[i]+s
    return s
