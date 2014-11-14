import numpy as np
from collections import Counter


def convert_text():
    fname1 = input("Please enter name of text file:")
    f = open(fname1, 'r')
    g = open('data', 'w')
    x = list(f)
    x = [ y.split() for y in x ]
    x = [ z for y in x for z in y ]
    cnt = Counter()
    for i in x:
        cnt[i] += 1
    y = []
    for i in cnt:
        y.append(cnt[i])
    y = list(map(str,y))
    y = ' '.join(y)
    g.write(y)
    f.close()
    g.close()
