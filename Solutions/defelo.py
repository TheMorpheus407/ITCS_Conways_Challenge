import numpy
N=lambda a,b:{(a+i%3-1,b+i//3-1)for i in range(9)if i-4}
def c(p,r):p={*(p or[])};[p:={x for w in p for x in N(*w)if 2-(x in p)<len(p&N(*x))<4}for _ in'*'*r];a,b=map(min,numpy.array([*p]or[(0,0)]).T);return[(x-a,y-b)for x,y in p]