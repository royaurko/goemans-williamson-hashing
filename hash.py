#!/usr/bin/env python3
import numpy as np
import generate_example as ge
import convert_text as ct


def generatekey(k, n):
    """Generate the key by sampling from a multivariate Gaussian"""
    mean = [0 for x in range(0, n)]
    cov = np.matrix(np.identity(n), copy=False)
    key = []
    for i in range(0, k):
        tmp = np.random.multivariate_normal(mean, cov)
        key.append(tmp)
    return key


def hashsingle(vec, k, key):
    """Hash a single vector using Goemans Williamson random hyperplane method"""
    hash_result = [int((np.sign(np.inner(y, vec))+1)/2) for y in key]
    hash_result = "".join(map(str, hash_result))
    return hash_result


def hash(arrayvec, k, n):
    """Hash a collection of vectors using hashsingle"""
    tempkey = generatekey(k, n)
    tempmap = [hashsingle(x, k, tempkey) for x in arrayvec]
    tempkey = [tuple(y) for y in tempkey]
    tempkey = tuple(tempkey)
    result = {tempkey: tempmap}
    return result


def collision(arrayvec, hashval):
    """Count number of collisions"""
    x = len(set(hashval))
    arrayvec = map(tuple, arrayvec)
    y = len(set(arrayvec))
    return y - x


if __name__ == '__main__':
    flag = input("Do you want to generate a random example?(y/n) ")
    fname1 = 'data'
    if flag == 'y':
        ge.generate_example()
    elif flag == 'n':
        flag2 = input("Do you want to hash a text file?(y/n) ")
        if flag2 == 'y':
            ct.convert_text()
        elif flag2 == 'n':
            fname1 = input("Please enter input filename:")
    fname2 = input("Please enter output filename:")
    f = open(fname1, 'r')
    g = open(fname2, 'w')
    x = [y.strip('\n').rstrip(' ') for y in list(f)]
    x = [[float(z) for z in y.split(' ')] for y in x]
    n = 0
    for i in x:
        if len(i) > n:
            n = len(i)
    for i in x:
        if len(i) < n:
            i.extend([0]*(n-len(i)))
    k = int(np.log2(n))
    k = k**2
    z = hash(x, k, n)
    for i in z:
        hashval = z[i]
        hashvalstr = '\n'.join(z[i])
    for i in range(0, len(hashvalstr)):
        g.write(hashvalstr[i])
    c = collision(x, hashval)
    print('Number of collisions=', c)
    print('Fraction of collisions=', c / len(x))
    f.close()
    g.close()
