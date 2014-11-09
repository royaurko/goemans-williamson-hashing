import numpy as np
import operator

def generatekey(k,n):
    """Generate the key by sampling from a multivariate Gaussian"""
    mean=[0 for x in range(0, n)]
    cov=np.matrix(np.identity(n), copy=False)
    key=[]
    for i in range(0,k):
        tmp=np.random.multivariate_normal(mean,cov)
        key.append(tmp)
    return key

def hashsingle(vec, k, key):
    """Hash a single vector using Goemans Williamson random hyperplane method"""
    hash_result=[int((np.sign(np.inner(y,vec))+1)/2) for y in key]
    hash_result="".join(map(str,hash_result))
    return hash_result


def hash(arrayvec, k, n):
    """Hash a collection of vectors using hashsingle"""
    tempkey=generatekey(k,n)
    tempmap=[hashsingle(x,k,tempkey) for x in arrayvec]
    tempkey=[tuple(y) for y in tempkey]
    tempkey=tuple(tempkey)
    result={tempkey:tempmap}
    return result


def collision(arrayvec,hashval):
     """Count number of collisions"""
     flag=0
     counter=0
     for i in range(0,len(arrayvec)):
         for j in range(0,i):
             if arrayvec[i]==arrayvec[j]:
                 flag=1
                 break
         if flag==1:
             continue
         else:
             for j in range(0,len(arrayvec)):
                 if arrayvec[j]!=arrayvec[j] and hashval[i]==hashval[j]:
                     counter+=1
     return counter


if __name__ == '__main__':
    fname1=input("Please enter input filename:")
    fname2=input("Please enter output filename:")
    f=open(fname1,'r')
    g=open(fname2,'w')
    x=[y.strip('\n').rstrip(' ') for y in list(f)]
    x=[[float(z) for z in y.split(' ')] for y in x]
    n=0
    for i in x:
        if len(i)>n:
            n=len(i)
    for i in x:
        if len(i)<n:
            i.extend([0]*(n-len(i)))
    k=int(np.log2(n))
    k=k**2
    z=hash(x,k,n)
    for i in z:
        hashval=z[i]
        hashvalstr='\n'.join(z[i])
    for i in range(0,len(hashvalstr)):
        g.write(hashvalstr[i])
    print('Number of collisions=',collision(x,hashval))
    f.close()
    g.close()

