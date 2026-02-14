from math import *
from time import *
from kandinsky import *
from random import *
from ion import *
fill_rect(0,0,340,340,'black')
draw_string("Fives",0,0,'white','black')
draw_string("Nights",0,15,'white','black')
draw_string("At",0,30,'white','black')
draw_string("Freddy-s",0,45,'white','black')
draw_string("EXE pour jouer",0,195,'white','black')
while not keydown(52):
  if randint(1,2)==1:
    fill_rect(250,50,340,340,'brown')
  else:
    fill_rect(250,50,340,340,'gray')

a=255
for i in range(255):
  fill_rect(0,0,340,340,(a,a,a))
  a=a-1
  sleep(0.01)
for i in range(5):
  fill_rect(0,0,340,340,'black')
  fill_rect(0,randint(1,11)*20,300,30,'white')
  draw_string("Night 1",130,100,'white','black')
  sleep(0.07)
fill_rect(0,0,340,340,(0,0,0))
draw_string("Night 1",130,100,'white',(0,0,0))  
sleep(3)
x=0
Power=100
t=0
lg=0
ld=0
pg=0
pd=0
cam=1
b=1
c=1
pc=1
pb=1
death=0
cm=100
bm=100
while t<300:
  t=t+0.03
  draw_string(str(300-t),0,195)
  fill_rect(x,0,10,340,(110,110,150))
  if pg==1:
    fill_rect(10+x,60,30,30,(245,0,0))
  else:
    fill_rect(10+x,60,30,30,(150,0,0))
  fill_rect(x+10,0,40,60,(110,110,150))
  fill_rect(x+10,90,40,10,(110,110,150))
  fill_rect(x+10,130,40,340,(110,110,150))
  if lg==1:
    fill_rect(10+x,100,30,30,(245,245,245))
  else:
    fill_rect(10+x,100,30,30,(150,150,150))
  if cm==0:
          if pc==5:
            if pd==1:
              pc==1
              cm=randint(300,600)
            else:
              death="c"
              time=360
              print("Chica→",pc,pd)
          else:
            pc=pc+1
            cm=randint(300,600)
  else:
    cm=cm-1
  if bm==0:
          if pb==5:
            if pg==1:
              pb=1
              bm=randint(300,600)
            else:
              death="b"
              time=360
          else:
            pb=pb+1
            bm=randint(300,600)
    
  else:
    bm=bm-1
              
  fill_rect(x+40,0,20,340,(110,110,150))
  if keydown(0) and x<0:
    x=x+5
  if keydown(3) and x>-295:
    x=x-5
  fill_rect(x+40,0,120,30,(110,110,150))  
  if pg==1:
    fill_rect(x+60,30,110,300,(150,150,150))
  else:
    if lg==0:
      fill_rect(x+60,30,110,300,(0,0,0))
    else:
      if b==0:
        fill_rect(x+60,30,110,300,(255,255,255))
      else:
        fill_rect(x+60,30,50,300,(0,0,250))
        fill_rect(x+110,30,60,300,'white')
  if x>-100 and keydown(4):
    if randint(1,10)==1:
      lg=0
    else:
      lg=1  
  else:
    lg=0
  if x<30 and keydown(52):
    if pg==0:
      pg=1
    else:
      pg=0
    while keydown(52):
        print("")
  fill_rect(x+170,0,20,340,(110,110,150))  
  fill_rect(x+190,0,200,150,(110,110,110))     
  fill_rect(x+190,150,200,350,(150,50,50))  
  fill_rect(x+440,0,10,340,(110,110,150))    
  if pd==1:
    fill_rect(x+450,30,110,300,(150,150,150))
  else:
    if ld==0: 
      fill_rect(x+450,30,110,300,'black')
    else:
      if c==0: 
        fill_rect(x+450,30,110,300,'white')
      else:
        if not randint(1,20)==1:
          fill_rect(x+450,30,60,300,'white')
          fill_rect(x+510,30,50,300,'yellow')
  if x<-110:
    if keydown(4):
      ld=1
    else:
      ld=0     
    if keydown(52):
      if pd==0:
        pd=1
      else:
        pd=0
      while keydown(52):
        print("")
    fill_rect(x+560,0,10,340,(110,110,150))    
    fill_rect(x+570,0,60,30,(110,110,150))
    if pd==1: 
      fill_rect(x+570,60,30,30,(245,0,0))
    else:
      fill_rect(x+570,60,30,30,(150,0,0))
    if ld==1:
      fill_rect(x+570,100,30,30,'white')
    else:
      fill_rect(x+570,100,30,30,(150,150,150))
    fill_rect(x+600,0,340,340,(110,110,150))
    if pc==5:
      c=1
    else:
      c=0
    if pb==5:
      b=1
    else:
      b=0
    if keydown(2):
      sleep(0.2)
      for i in range(20):
        fill_rect(0,200-i*15,340,300,'black')
      while not keydown(2):
        fill_rect(30,0,270,340,(110,110,110))
        if cam==pb:
          fill_rect(0,0,30,340,'blue')
        else:
          fill_rect(0,0,340,340,(110,110,110))
        if cam==pc: 
          fill_rect(270,0,30,340,'yellow')
        else:
          fill_rect(270,0,30,340,(110,110,110))
        fill_rect(300,0,340,190,'gray')
        fill_rect(300,(cam-1)*50,340,50,'green')
        draw_string(str(Power),283,200)
        if keydown(0) and cam>1:
          cam=cam-1
          sleep(0.2)
        if keydown(3) and cam<4:
          cam=cam+1
          sleep(0.2)      
        Power=Power-0.001            
        t=t+0.03
        if cm==0:
          if pc==5:
            if pd==1:
              pc==1
              cm=randint(300,600)
            else:
              death="c"
              time=360
              print("porte",pd)
          else:
            pc=pc+1
            randint(300,600)
        else:
          cm=cm-1
        if bm==0:
          if pb==5:
            if pg==0:
              death="b"
              time=360
            else:
              pb=1
              bm=randint(300,600)
          else:
            pb=pb+1
            bm=randint(300,600)
        else:
          bm=bm-1
      i=0              
      for i in range(20):
       fill_rect(i*15,0,340,300,'black')
      sleep(0.1)
if death==0:
  fill_rect(0,0,340,340,'black')
  draw_string("5 AM",130,100,'white','black')
  sleep(1)
  draw_string("6",130,107,'white','black')
  sleep(1)
  fill_rect(0,0,340,340,'black')
  draw_string("6 AM",130,100,'white','black')
else:
  for i in range(40):
    if death=="c":
      fill_rect(0,0,340,340,(0,0,0))
      fill_rect(randint(40,60),0,200,300,'yellow')    
    else:
      fill_rect(0,0,340,340,(0,0,0))
      fill_rect(randint(40,60),0,200,300,'blue')
  fill_rect(0,0,340,340,'black')     
  while True:
    if randint(1,2)==1:
      fill_rect(0,0,340,340,'black') 
    else:
      fill_rect(0,0,340,340,'gray') 
    draw_string("Perdu",0,190,'white','black')
