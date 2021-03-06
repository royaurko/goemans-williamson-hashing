import random


def generate_example():
    k = int(input('Dimension of the data:'))
    if k <= 0:
        raise ValueError('bad argument')
    n = int(input('Number of vectors you want to generate:'))
    if n <= 0:
        raise ValueError('bad argument')
    a = float(input('Lowerbound on entries:'))
    b = float(input('Upperbound on entries:'))
    fname = input('Enter name of file to write data to:')
    temp = []
    tempstr = ""
    f = open(fname, 'w')
    for i in range(0, n):
        for j in range(0, k):
            temp.append(random.uniform(a, b))
        tempstr = list(map(str, temp))
        tempstr = ' '.join(tempstr)
        f.write(tempstr)
        f.write('\n')
        temp, tempstr = [], ""
