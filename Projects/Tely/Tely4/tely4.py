from kandinsky import *
a=fff=ins=0
try:from telyapp import *
except:a=1
try:from savetely import *
except:a=2
if a>0:
 fff=1
 print("Il manque ce script")
 if a==1:print("-telyapp")
 else:print("-savetely")
 print("Ou il est peut etre\nrenomer")
def dess(num):
 fill_rect(0,0,340,340,['white','black'][tsave(0,6)[0]])
 if num==0 or num>tsave(0,2):num=1
 pal=tsave(num,0)[0]
 im=tsave(num,1)[1]
 r=i=0
 z=len(im)
 while r<z:
  s = im[r]
  n=""
  r+=1
  while r<len(im) and "9">=im[r] >="0":
   n+=im[r]
   r+=1
  nb = 1 if n=="" else int(n)  
  c = pal[ord(s)-65]
  for j in range(nb):
   fill_rect(4*(i%80),4*(i//80),4,4,(c[0],c[1],c[2]))
   i+=1 
def ar():
 global se,pp,be,col,ze,ee
 if se>0:
  for j in range(3):col[j]+=ze[j]
  ee=ee+1+(se-1)*-1
  fill_rect(0,0,340,20,col)
 else:
  if pp!=col:
   se=ee=0
   pp=get_pixel(1,150)
   pp=(pp[0]*0.9,pp[1]*0.9,pp[2]*0.9)
   pp=list(pp)
   ze,col=[],list(pp)
   for i in range(3):ze.append((pp[i]-be[i] if pp[i]<be[i]*5 else be[i]-pp[i])/500)
   fill_rect(0,0,340,20,col)
 hr(130,2,tuple(col))
def hr(x,y,c):
 n=monotonic()-td+tsave(0,6)[2][0]*3600+tsave(0,6)[2][1]*60
 j=n//86400
 h=int((n-j*86400)//3600)
 m=str(int((n-3600*h-86400*j)//60))
 h=str(h)
 draw_string(["0",""][len(h)-1]+h+":"+["0",""][len(m)-1]+m,x,y,['white','black'][(220,220,220)<c],c)
#from ion import *
from time import *
no=bq=tq=es=0
mt,td=tsave(0,0),[tsave(0,6)[2][2],monotonic()][tsave(0,6)[2][2]==0]
be=(0,255,0)
col,djop,ze=1,[],[]
while fff<1:
  s=monotonic()
  if no<2:     
    no=0
    if bq>0:
     fill_rect(0,0,340,340,(20,20,20))
     if bq==1:draw_string("Verrouiller "+str(int(tq+25-monotonic()))+"s",85,150,(10,10,10))
    else:dess(tsave(0,1))
    while not keydown(4) and s+10>monotonic() and (tq+25>monotonic() or bq==0):hr(0,150,get_pixel(2,148))
    if tq+25<monotonic() and bq==1:
     bq=no=0
     es=1
  if no<3:
   for i in range(50):
    for j in range(50):
     a=get_pixel(j*20+1,(i-j)*20+1)
     a=(a[0]*0.3,a[1]*0.3,a[2]*0.3)
     fill_rect(j*20,(i-j)*20,20,20,['black',a][s>monotonic()-10])
  if s>monotonic()-10 and no<4 and bq!=1:
    b,no="",0
    s=monotonic()
    draw_string("_"*4,140,140,'white',get_pixel(138,148))
    draw_string("Saisir code",105,50,'white',get_pixel(115,50))
    h=[48,42,43,44,36,37,38,30,31,32,17]
    while len(b)<4 and s+20>monotonic():
      i=0
      while i<11 and len(b)<4:
       if keydown(h[i]):
        s=monotonic()
        if i==10:
          if b=="":b,no="<<>>",1
          else:
           j=""
           for a in range(len(b)-1):j+=b[a]
           b=str(j)
        else:b+=str(i)          
        draw_string(b+"_"*(4-len(b)),140,140,'white',get_pixel(138,148))
        s=monotonic()+0.3
        while keydown(h[i]) and s>monotonic():pass
       i+=1
    if s+20<monotonic():no=0
    else:     
     if b[0]!="<": 
      j=""
      for i in range(4):j+=str(ord(mt[i]))[1]
      print(j,b)
      if j==b:
        b=j=es=mx=my=pz=k=fl=ee=se=pp=0
        g,f,msave=monotonic(),1,list(tsave(0,-1))
        dess(tsave(0,3))
        while keydown(4):pass
        while g+35>monotonic():
         if keydown(0) and mx>0:mx,f=mx-1,2
         if keydown(3) and mx<3 and mx+my*4<=len(tsave(0,4))-2:mx,f=mx+1,5
         if keydown(1) and my>0:my,f=my-1,3
         if keydown(2) and my<1 and len(tsave(0,4))>4:my,mx,f=my+1,[len(tsave(0,4))-5,mx][mx+my*4+4<=len(tsave(0,4))-1],4
         if f>0:
          i=len(tsave(0,4)) if len(tsave(0,4))<9 else 8
          for i in range(i):dapp([2,tsave(0,4)[i]][7>i or len(tsave(0,4))<9],[35,50][i==mx+my*4],17,i*70+[30,-250][int(i/4)],[40,120][int(i/4)])
          g=monotonic()+0.3
          if f>1:
           while keydown(f-2) and g>monotonic():pass
          f=0
         if keydown(4) and k<1:
          g=monotonic()+0.5
          while keydown(4) and g>monotonic():pass
          if keydown(4):ex,ey,k=mx,my,1
          else:
           a=1
           if not(mx+my*4<7 or len(tsave(0,4))<9):a=opn(1)
           if a>0:
            if not tsave(0,4)[[mx+my*4,a][a>6]] in djop:
              a,t=dapp(tsave(0,4)[[mx+my*4,a][a>6]],50,0,0,0),30
              x,y=int(160-t*1.5),int(110-t*1.5)
              for i in range(2):
               for j in range(2):fill_rect(x-int(t/2)+i*t*3,y-int(t/2)+j*t*3,t,t,get_pixel(0,0))
              g=2+monotonic()
              while not keydown(52) and g>monotonic():pass
              print(tsave(0,4))
              a=0
              print(tsave(0,4)[[mx+my*4,a][a>6]])
              if not keydown(52):djop.append(tsave(0,4)[[mx+my*4,a][a>6]])
            ret=""
            if not keydown(52):ret=opn(tsave(0,4)[mx+my*4])
            if type(ret)!="NoneType" and type(ret)!="str":
              i=tsave(0,4)[mx+my*4]
              if i==3:
                try:td=ret[6][2][2]
                except:i=-1
                if i>-1:sm(ret)
           dess(tsave(0,1))
           while keydown(52):pass
           f,g,pp=1,monotonic(),0
         if k>0 and not keydown(4):
          if i<8 or len(tsave(0,4))<9:
           if keydown(17):
            msave,f,k=tsave(0,-1),0,1
            msave[4].pop(ex+4*ey)
            msave[5].pop(ex+4*ey)
            sm(msave)
            if len(tsave(0,4))<8:
              dess(tsave(0,3))
              f=pp=1
            if mx+my*4>len(tsave(0,4))-2:mx=my=0
           else:
            if len(tsave(0,4))<9 or (mx+my*4!=8 and ex+ey*4!=8):
             fill_rect(mx*70+30,my*80+95,55,22,get_pixel(mx*70+30,my*80+95))
             fill_rect(ex*70+30,ey*80+95,55,22,get_pixel(ex*70+30,ey*80+95))
             msave[4][mx+my*4],msave[4][ex+ey*4],msave[5][mx+my*4],msave[5][ex+ey*4],k,f=msave[4][ex+ey*4],msave[4][mx+my*4],msave[5][ex+ey*4],msave[5][mx+my*4],0,1
             sm(msave)
           k=0
         if keydown(52):
          g=0.5+monotonic()
          while keydown(52) and g>monotonic():pass
          if keydown(52):break
         if k>0 and keydown(17):
          fill_rect(ex*70+30,ey*80+40,51,51,'red')
          fill_rect(ex*70+43,ey*80+50,25,35,'white')
          fill_rect(ex*70+35,ey*80+55,41,5,'white')
          fl=1
         if fl>0 and not keydown(17):fl,f=0,1
         ar()
        no=0
      else:
        es+=1
        if es>2:
          no=bq=1
          tq=monotonic()
        for i in range(4):
         j=""
         for a in range(4-i):j+=b[a]
         draw_string(j+i*"_",140,140,'red',get_pixel(138,148))
         sleep(0.05)
        if es<3:
         no=3
  if no==0:
   fill_rect(0,0,340,340,'black')
   while keydown(52):pass
   while not keydown(52):pass
