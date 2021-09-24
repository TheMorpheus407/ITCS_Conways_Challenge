def c(p,r):
 if p==None:return[]
 for k in range(r):p={(a+c,b+d)for c in(-1,0,1)for d in(-1,0,1)for a,b in p if((a+c,b+d)in p)+4>sum(abs(a+c-e+(b+d-f)*1j)<2for e,f in p)>2}
 s=lambda n:min([t[n]for t in p]);return[(x-s(0),y-s(1))for x,y in p]
