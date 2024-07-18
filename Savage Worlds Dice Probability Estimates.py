import sys
import random
Die = sys.argv[1]

W = sys.argv[2]

It = int(sys.argv[3])

Adj = sys.argv[4]

o = 0
wo = 0
outs = []
c = True
s = 1234
wc=True
for i in range(1, It + 1):
    r=0
    o=0
    c = True
    wc = True
    wo=0
    wr=0
    while c == True:
        random.seed(s)
        d1 = range(1, int(Die) + 1)
        r = int(random.choice(d1))
        if r != Die:
            o = o + r
            c = False
        else:
            o = o + r
        s=s+i
    if W == True:
        while wc==True:
            random.seed(s)
            s=s+i
            d2 = range(1,7)
            wr = int(random.choice(d2))
            if wr != 6:
                wo=wo+wr
                wc = False
            else:
                wo=wo+wr
    if wo>o:
        outs.append(wo)
    else:
        outs.append(o)
print(outs)
import numpy as np
mean = str(np.mean(outs)+Adj)
sd = str(np.std(outs))
print("You expect to get a "+mean+" with a standard deviation of "+ sd)
hits=sum(1 for item in outs if item>(3-Adj))
raises=sum(1 for item in outs if item>(7-Adj))
fails = sum(1 for item in outs if item==1)
print("Hits:")
print(hits/It)
print("Raises:")
print(raises/It)
print("Fails:")
print(fails/It)
