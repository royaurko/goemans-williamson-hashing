import random

if __name__ == '__main__':
    k=int(input('Dimension of the data:'))
    if k<=0:
        raise ValueError('bad argument')
    n=int(input('Number of vectors you want to generate:'))
    if n<=0:
        raise ValueError('bad argument')
    a=float(input('Lowerbound on entries:'))
    b=float(input('Upperbound on entries:'))
    temp=[]
    tempstr=""
    f=open('text','w')
    for i in range(0, n):
        for j in range(0,k):
            temp.append(random.uniform(a, b))
        tempstr=list(map(str,temp))
        tempstr=' '.join(tempstr)
        f.write(tempstr)
        f.write('\n')
        temp,tempstr=[],""

