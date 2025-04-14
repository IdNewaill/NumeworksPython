from math import *
from kandinsky import *
from random import *
#from ion import *
from time import *
x=0
y=0
px=0
py=0
t=50
lon=8
lar=6
m=[[0,0]for i in range(lon*lar)]
m[0]=[1,0]
m[1]=[6,0]
m[2]=[5,0]

def w_bloc(x,y,d):
  try:
    if d==0:
      return m[x-1+y*lon]
    if d==1:
      return m[x+(y-1)*lon]
    if d==2:
      return m[x+(y+1)*lon]
    if d==3:
      return m[x+1+y*lon]
  except:return [0,0]
pp=0
while True:
  #fill_rect(0,0,340,340,(0,0,0))
  for ix in range(7):
    for iy in range(5):
      n=m[(y+iy)*lon+x+ix]
      #draw_string(str(n[1]),ix*t,iy*t)
      if n[0]<10:
        fill_rect(ix*t,iy*t,t,t,(0,[200,255][ix==px and iy==py],[100,0][((y+iy)*(lon+1)+x+ix)%2]))
        if n[0]==1:
          c=(200-(15-n[1])*10,0,0)
          draw_string(str(n[1]),ix*t,iy*t)
          if w_bloc(x+ix,y+iy,0)[0]!=0:
            fill_rect(ix*t,iy*t+int(t/3),int(t/2),int(t/3),c)
          if w_bloc(x+ix,y+iy,1)[0]!=0:
            fill_rect(ix*t+int(t/3),iy*t,int(t/3),int(t/2),c)
          if w_bloc(x+ix,y+iy,2)[0]!=0:
            fill_rect(ix*t+int(t/3),iy*t+int(t/2),int(t/3),int(t/2),c)
          if w_bloc(x+ix,y+iy,3)[0]!=0:
            fill_rect(ix*t+int(t/2),iy*t+int(t/3),int(t/2),int(t/3),c)
          fill_rect(ix*t+int(t/3),iy*t+int(t/3),int(t/3),int(t/3),c)
        elif 1<n[0]<6:
          fill_rect(ix*t,iy*t,t,t,(200,)*3)
          draw_string(str(n[1]),ix*t,iy*t)
          if n[0]==2:
            fill_rect(ix*t+int(t/5),iy*t+int(t/5)*2,int(t/5)*2,int(t/5),(200,0,0))
            fill_rect(ix*t+int(t/5)*4,iy*t+int(t/5)*2,int(t/5),int(t/5),(150,100,0))
          if n[0]==3:
            fill_rect(ix*t+int(t/5)*2,iy*t+int(t/5),int(t/5),int(t/5)*2,(200,0,0))
            fill_rect(ix*t+int(t/5)*2,iy*t+int(t/5)*4,int(t/5),int(t/5),(200,100,0))
          if n[0]==4:
            fill_rect(ix*t+int(t/5)*2,iy*t,int(t/5),int(t/5),(200,100,0))
            fill_rect(ix*t+int(t/5)*2,iy*t+int(t/5)*2,int(t/5),int(t/5)*2,(200,0,0))
          if n[0]==5:
            fill_rect(ix*t,iy*t+int(t/5)*2,int(t/5),int(t/5),(200,100,0))
            fill_rect(ix*t+int(t/5)*2,iy*t+int(t/5)*2,int(t/5)*2,int(t/5),(200,0,0))
        elif n[0]==6:
          fill_rect(ix*t+int(t/4),iy*t+int(t/4),int(t/2),int(t/2),(255,100*n[1],0))
          draw_string(str(n[1]),ix*t,iy*t)
        elif n[0]==7:
          fill_rect(ix*t+int(t/5),iy*t+int(t/3),int(t/5)*3,int(t/3),(155+(n[1]==0)*40,)*3)
        elif n[0]==8:
          fill_rect(ix*t+int(t/3),iy*t+int(t/5),int(t/3),int(t/5)*3,(155,155,155))
          fill_rect(ix*t+int(t/5)*2,iy*t+int(t/6),int(t/5),int(t/6)*(2+n[1]>0),(199,100,90))
      else:
        if n[0]==10:
          fill_rect(ix*t,iy*t,t,t,(255,0,0))
        if n[0]==11:
          fill_rect(ix*t,iy*t,t,t,(150+(n[1]==1)*95,)*3)
        if n[0]==12:
          fill_rect(ix*t+int(t/4),iy*t+int(t/4),int(t/2),int(t/2),(255,0,0))
        if n[0]==13:
          fill_rect(ix*t,iy*t,t,t,(196,149,53))
  for ix in range(lon):
    for iy in range(lar):
      n=m[iy*lon+ix]
      if n[0]==1:
       m[iy*lon+ix][1]=max(max([w_bloc(ix,iy,i)[1]for i in range(4)])-1,max([w_bloc(ix,iy,i)[1]*15 for i in range(4)if w_bloc(ix,iy,i)[0]==2+i]+[0]))
      if 1<n[0]<6:
       m[iy*lon+ix][1]=1*(1<w_bloc(ix,iy,n[0]-2)[1])
      if n[0]==6:
       m[iy*lon+ix][1]=16-16*max([w_bloc(ix,iy,i)[1]for i in range(4)if w_bloc(ix,iy,i)[0]==2+i]+[0])
      elif n[0]==7:
       m[iy*lon+ix][1]=16*(not(not(keydown(4))or px+x!=ix or py+y!=iy))
      elif n[0]==8:
        if px+x==ix and py+y==iy:
         if keydown(4) and pp==0:
           m[iy*lon+ix][1]=16-m[iy*lon+ix][1]
           pp=1
         if not keydown(4):
           pp=0
      if n[0]==11:
       m[iy*lon+ix][1]=1*1<max(max([w_bloc(ix,iy,i)[1]for i in range(4)])-1,max([w_bloc(ix,iy,i)[1]*15 for i in range(4)if w_bloc(ix,iy,i)[0]==2+i]+[0]))
    if keydown(16):
      if m[(y+py)*lon+px+x][0]==13:
        m[(y+py)*lon+px+x][0]=1
      else:
        m[(y+py)*lon+px+x][0]+=1
      m[(y+py)*lon+px+x][1]=16*(m[(y+py)*lon+px+x][0]==10)
      print(m[(y+py)*lon+px+x])
      while keydown(16):pass
    if keydown(17):
      m[(y+py)*lon+px+x]=[0,0]
      while keydown(17):pass
  s=-1
  if keydown(4):
    if keydown(0)and px>0:px,s=px-1,0
    if keydown(3)and px<7:px,s=px+1,3
    if keydown(1)and py>0:py,s=py-1,1
    if keydown(2)and py<5:py,s=py+1,2
  else:
    if keydown(0)and x>0:x,s=x-1,0
    if keydown(3)and x<lon-7:x,s=x+1,3
    if keydown(1)and y>0:y,s=y-1,1
    if keydown(2)and y<lar-5:y,s=y+1,2
  if s>-1:
    while keydown(s):pass
    s=-1
