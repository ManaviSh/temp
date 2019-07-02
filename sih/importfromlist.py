# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:38:42 2019

@author: thnxe
"""



import pandas as pd
df = pd.read_excel('trip.xlsx', sheet_name=0) 
mylist = df['Inclination'].tolist()
time = df['Time'].tolist()
take_speed = df['Speed'].tolist()
theta=[]
s2 = []
for i in mylist:
    if(i<-1.57):
        theta.append(0)
    if(i<-1.47 and i>=-1.57):    
        theta.append(1)
    if(i<-1.37 and i>=-1.47):    
        theta.append(2)
    if(i<-1.27 and i>=-1.37):    
        theta.append(3)
    if(i<-1.17 and i>=-1.27):    
        theta.append(4)
    if(i<-1.07 and i>=-1.17):    
        theta.append(5)
    if(i<-0.97 and i>=-1.07):    
        theta.append(6)
    if(i<-0.87 and i>=-0.97):    
        theta.append(7)
    if(i<-0.77 and i>=-0.87):    
        theta.append(8)
    if(i<-0.67 and i>=-0.77):    
        theta.append(9)
    if(i<-0.57 and i>=-0.67):    
        theta.append(10)
    if(i<-0.47 and i>=-0.57):    
        theta.append(11)
    if(i<-0.37 and i>=-0.47):    
        theta.append(12)
    if(i<-0.27 and i>=-0.37):    
        theta.append(13)
    if(i<-0.17 and i>=-0.27):    
        theta.append(14)
    if(i<-0.07 and i>=-0.17):    
        theta.append(15)
    if(i<0.03 and i>=-0.07):    
        theta.append(16)
    if(i<0.13 and i>=0.03):    
        theta.append(17)
    if(i<0.23 and i>=0.13):    
        theta.append(18)
    if(i<0.33 and i>=0.23):    
        theta.append(19)
    if(i<0.43 and i>=0.33):    
        theta.append(20)
    if(i<0.53 and i>=0.43):    
        theta.append(21)
    if(i<0.63 and i>=0.53):    
        theta.append(22)
    if(i<0.73 and i>=0.63):    
        theta.append(23)
    if(i<0.83 and i>=0.73):    
        theta.append(24)
    if(i<0.93 and i>=0.83):    
        theta.append(25)
    if(i<1.03 and i>=0.93):    
        theta.append(26)
    if(i<1.13 and i>=1.03):    
        theta.append(27)
    if(i<1.23 and i>=1.13):    
        theta.append(28)
    if(i<1.33 and i>=1.23):    
        theta.append(29)
    if(i<1.43 and i>=1.33):    
        theta.append(30)
    if( i>=1.43):    
        theta.append(31)
for j in take_speed:
    if(j==0):
        s2.append(1)
    if(j==1):
        s2.append(2)
    if(j==2):
        s2.append(3)
    if(j==3):
        s2.append(4)
    if(j==4):
        s2.append(5)
    if(j==5):
        s2.append(6)
    if(j==6):
        s2.append(7)
    if(j==7):
        s2.append(8)
    if(j==8):
        s2.append(9)
    if(j==9):
        s2.append(10)
    if(j==10):
        s2.append(11)
    if(j==11):
        s2.append(12)
    if(j==12):
        s2.append(13)
    if(j==13):
        s2.append(14)
    if(j==14):
        s2.append(15)
    if(j==15):
        s2.append(16)
    if(j==16):
        s2.append(17)    
    if(j==17):
        s2.append(18)
    if(j==18):
        s2.append(19)
    if(j==19):
        s2.append(20)
    if(j==20):
        s2.append(21)
    if(j==21):
        s2.append(22)
    if(j==22):
        s2.append(23)
    if(j==23):
        s2.append(24)
    if(j==24):
        s2.append(25)
    if(j==25):
        s2.append(26)
    if(j==26):
        s2.append(27)
    if(j==27):
        s2.append(28)
    if(j==28):
        s2.append(29)
    if(j==29):
        s2.append(30)
    if(j==30):
        s2.append(31)
    if(j==31):
        s2.append(32)
    if(j==32):
        s2.append(33)
    if(j==33):
        s2.append(34)
    if(j==34):
        s2.append(35)
    if(j==35):
        s2.append(36)
    if(j==36):
        s2.append(37)
print(max(theta))
curr_state=list(zip(time,theta))
next_states=list(zip(time,theta[1:]))
next_actions=list(zip(time,s2))
        