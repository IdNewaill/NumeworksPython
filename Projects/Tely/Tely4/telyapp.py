from math import *
from kandinsky import fill_rect as fr, draw_string as dr,get_pixel
from ion import keydown as ki
from savetely import *
from time import *
ins,ans=0,-1
def dess(num,pq,x,y):
 fr(0,0,340,340,['white','black'][tsave(0,6)[0]])
 if num==0 or num>tsave(0,2):num=1
 pal=tsave(num,0)[0]
 im=tsave(num,1)[1]
 r = 0
 i=0
 while r<len(im):
  s = im[r]
  n=""
  r+=1
  while r<len(im) and "9">=im[r] >="0":
   n+=im[r]
   r+=1
  nb = 1 if n=="" else int(n)  
  c = pal[ord(s)-65]
  for j in range(nb):
   fr(4*(i%80),4*(i//80),4,4,(c[0],c[1],c[2]))
   i+=1 
def opn(d):
 fr(0,0,340,340,['white','black'][tsave(0,6)[0]])
 n=['white','black'][tsave(0,6)[0]]
 k=['black','white'][tsave(0,6)[0]]
 while ki(4):pass
 if d<1:
  global ins,ans
  nbr=5
  ta,s,p=1,3,0
  ak=[0,0,0,0,1,0]
  af=0 if d==(0,0,0) else 1
  q,qa=nbr,0
  while not ki(52):
    a=[ki(0),ki(1),ki(2),ki(3)]
    if a==[True,False,False,False] and p>0:p,s=0,3
    if a==[False,False,False,True] and p<1:p,s=1,3
    if s>0:
     fr(0,0,320,320,[(230,230,230),(50,50,50),n,n][tsave(0,6)[0]+p*2])
     if p<1:
      fr(0,0,320,40,n)
      dr("TelyApp+",10,10,k,n)
      for i in range(2):
        fr(10,50+i*60,300,50,[n,k][qa==i])
        dapp(q-i,50,7,40,53+i*60)
     else:
      fr(0,179,320,1,k)
      fr(0,40,320,1,k)
     fr(0,180,320,45,n)
     fr(p*160,215,160,5,(0,150,255))
     dr("Accueil",45,187,[(0,150,255),(200,200,200)][p],n)
     dr("Rechercher",185,187,[(200,200,200),(0,150,255)][p],n)
     if s<3:
      i=monotonic()+0.3
      while ki(s) and i>monotonic():pass
     s=0
    if p<1:
     if ki(1):
      if qa>0:qa,s=0,1
      elif q<nbr:q,s=q+1,1
     if ki(2):
      if qa<1:qa,s=1,2
      elif q>1:q,s=q-1,2
     if ki(4):
      while ki(4):pass
      fr(0,0,340,340,n)
      dapp(q-qa,50,20,20,20)
      dr("Description",12,130,k,n)
      fr(10,150,300,70,[(230,230,230),(50,50,50)][tsave(0,6)[0]])
      while not ki(17):
       i=str(int((monotonic()-ins)/20*-100))+"%"
       dr([i+(6-len(i))*" ",["Instal","Ouvrir"][q-qa in tsave(0,4)]][ins<1 or ans!=q-qa],200,70,k,['orange','blue'][q-qa in tsave(0,4) and ans!=q-qa])
       dr(["Utilitaire","Jeux"][ak[q-qa]],180,33,'gray',n)
       if ki(4):
        if q-qa in tsave(0,4):return opn(q-qa)
        elif ins==0:ins,ans=monotonic()+20,q-qa
       if ins>0 and monotonic()>ins:
        i=tsave(0,-1)
        i[4].append(ans)
        sm(i)
        ins,ans=0,-1
      s=3
 if d==1:
  fe,on=1,7
  while ki(4):pass
  while not ki(52):
   if ki(0) and on>7:on,fe=on-1,1
   if ki(3) and on<len(tsave(0,4))-1:on,fe=on+1,4
   if ki(4):return on
   if fe>0:
    fr(0,30,320,130,get_pixel(110,150))
    dapp(tsave(0,4)[on],50,27,50,50)
    i=get_pixel(40,51)
    j=['white','black'][(220,220,220)<i]
    if on<len(tsave(0,4))-1:
     dapp(tsave(0,4)[on+1],30,27,200,50)
     dr(">",300,83,j,i)
    if on>7:dr("<",20,83,j,i)
    k=0.3+monotonic()
    while ki(fe-1) and k>monotonic():pass
    fe=0
  return 0
 if d==2:
   dess(2,0,0,4)
   while not ki(52):pass  
 if d==4:
  score = 0
  dx,dy = 0,1
  vert,rouge = (0,255,0),(255,0,0)
  s = [[160,110]]
  food = True
  pt = monotonic()
  while True:
    ct = monotonic()
    dt = ct-pt
    if food:
      fx = 10 * randint(0,31)
      fy = 10 * randint(0,21)
      food = False
    fill_rect(fx,fy,10,10,rouge)
    if keydown(KEY_UP): dx,dy = 0,-1
    if keydown(KEY_DOWN) : dx,dy = 0,1
    if keydown(KEY_LEFT): dx,dy = -1,0
    if keydown(KEY_RIGHT): dx,dy = 1,0
    if dt>.2-.02*v:
      pt = monotonic()
      x = s[0][0] + 10*dx
      y = s[0][1] + 10*dy
      if x<0 or x>310 or y<0 or y>210 or get_pixel(x,y)==vert:
        draw_string("oups !!",5,10)
        fill_rect(x,y,10,10,rouge)
        return score
      s.insert(0,[x,y])
      if get_pixel(x,y)!=rouge:
        q = s.pop()
        fill_rect(q[0],q[1],10,10,(248,255,248))
      else:
        score += 1
        draw_string(str(score),5,10)
        food=True
      fill_rect(s[0][0],s[0][1],10,10,vert)
 if d==3:
  x=y=40
  on=tsave(0,6)
  b=["Theme sombre","Notifications","Heure"]
  m,f,a=0,1,tsave(0,-1)
  while not ki(52):
   if f>0:
    fr(0,0,340,340,['white','black'][tsave(0,6)[0]])
    fr(15,4+m*30,300,30,(175,175,175))
    for i in range(len(on)):
      if i==2:dr(["","0"][len(str(on[i][0]))==1]+str(on[i][0])+":"+["","0"][len(str(on[i][1]))==1]+str(on[i][1]),200,10+i*30,['black','white'][tsave(0,6)[0]],[['white','black'][tsave(0,6)[0]],(175,175,175)][m==i])
      else:bt(200,10+i*30,on[i])
      dr(b[i],20,10+i*30,['black','white'][tsave(0,6)[0]],[['white','black'][tsave(0,6)[0]],(175,175,175)][m==i])
    while ki([f,4][f>2]):pass
    f=0
   if ki(4):
    if m==2:on[m]=[tos(200,10+m*30,2,24,on[m][0]),tos(230,10+m*30,2,59,on[m][1]),monotonic()]
    else:on[m]=[1,0][on[m]]
    a[6][m]=on[m]
    print(a)
    sm(a)
    f=3
   if ki(1) and m>0:m,f=m-1,1
   if ki(2) and m<len(on)-1:m,f=m+1,2
  return a
 if d==5:
  tim=monotonic()
  j=p=0
  s=1
  while not ki(52):
    if p<1:
     if j==0:
      a=(str(int((monotonic()-tim)/60)),str(int((monotonic()-tim)%60)))
      dr(["0",""][len(a[0])-1]+a[0]+":"+["0",""][len(a[1])-1]+a[1],132,150,['black','white'][tsave(0,6)[0]],['white','black'][tsave(0,6)[0]])
     if j>0.00:dr(["0",""][len(a[0])-1]+a[0]+":"+["0",""][len(a[1])-1]+a[1],132,150,['white','black'][tsave(0,6)[0]],['black','white'][tsave(0,6)[0]])
     if ki(4):
      s=monotonic()+0.5
      while ki(4) and s>monotonic():pass
      if s>monotonic():
        if j>0:tim,j=monotonic()-j,0
        else:j=monotonic()-tim
      else:tim,j=0,0.01
      s=0
      while ki(4):pass
    if ki(0) and p>0:p,s=0,3
    if ki(3) and p<1:p,s=1,3
    if s>0:
     fr(0,0,320,320,[(230,230,230),(50,50,50),n,n][tsave(0,6)[0]+p*2])
     if p<1:
      dapp(5,50,35,105,40)
     else:
      fr(0,0,320,40,n)
      for i in range(2):
       fr(10,50+i*60,300,50,n)
       dapp(5,50,7,40,53+i*60)
       bt(40,253,tsave(0,7)[i][2])
     fr(0,180,320,45,n)
     fr(p*160,215,160,5,(0,150,255))
     dr("Timer",45,187,[(0,150,255),(200,200,200)][p],n)
     dr("Alarmes",185,187,[(200,200,200),(0,150,255)][p],n)
     if s<3:
      o=monotonic()+0.3
      while not ki(s) and o>monotonic():pass
     s=0
def tos(x,y,o,ox,e):
 h,j=[48,42,43,44,36,37,38,30,31,32,17],""
 while ki(4):pass
 while not ki(4) and len(j)<o:
  for i in range(11):
   if ki(h[i]) and (len(j)<o or i>10):
    if ox>=int(j+str(i)):j+=str(i)
    else:
     a=""
     for k in range(len(j)-2):
      a+=j[k]
     if i<10:a+=str(i)
     j=a
    s=0.3+monotonic()
    while ki(h[i]) and s>monotonic():pass
  dr(j+"_"*(o-len(j)),x,y,['white','black'][(220,220,220)<get_pixel(x,y)],get_pixel(x,y))
 if j=="":j=e
 else:j=int(j)
 return j
def bt(x,y,n):
 fr(x,y,40,20,['red','green'][n])
 fr(x+5+n*20,y+5,10,10,'white')
def dapp(d,da,t,x,y):
 #nom,image,auteur,jeux?=1
 a=[("app+","025000"+"025"*4+"000025000","idaill",0),
 ("Autre","530"*2+"550"*7,"?",0),
 ("Image","035500530020555550030040050","idaill",0),
 ("Para.","222"+"333555"*3+"333222","idaill",0),
 ("snake","5"*9+"040"*2+"5"*9+"500","idaill",1),
 ("Timer","444000444555000000444000444","idaill",0)
   ][d]
 if t==0:
  t=30
  x,y=int(160-t*1.5),int(110-t*1.5)
  fr(0,0,340,340,(int(a[1][12])*40,int(a[1][13])*40,int(a[1][14])*40))
 for i in range(3):
  for j in range(3):
   c=i*3+j*9
   c=(int(a[1][c])*da,int(a[1][c+1])*da,int(a[1][c+2])*da)
   fr(i*t+x,j*t+y,t,t,c)
 dr(a[0],x+int(t*1.5-(len(a[0])/2)*10),y+t*3+[5,20][da==0],['black','white'][(220,220,220)>get_pixel(x,y+t*3+5)],get_pixel(x,y+t*3+5))
