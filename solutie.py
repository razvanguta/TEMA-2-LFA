f=open("automat.in","r")
starein=int(f.readline())
nrstfin=int(f.readline())
sirstfin=f.readline()
starefin=[int(x) for x in sirstfin.split()]
nrtranz=int(f.readline())
tranz=[]
for i in range(nrtranz):
    inp=f.readline()
    inp=inp.split()
    tranz.append([int(inp[0]),int(inp[1]),inp[2]])
LAFN=[]*101
for x in range(101):
    LAFN.append([])
for x in tranz:
    ok=False
    for y in LAFN[x[0]]:
        if y[0]==x[2]:
            y[1].add(x[1])
            ok=True
    if ok==False:
        LAFN[x[0]].append([x[2],{x[1]}])
viitor=[]
viz=[]
viitor.append({starein})
viz.append({starein})
while(len(viitor)!=0):
    actual=viitor.pop(0)
    lauxtot=[]
    for x in actual:
        laux=[]
        for y in LAFN[x]:
            laux.append(y.copy())
        for y in laux:
            lauxtot.append(y.copy())

        for w in lauxtot:
            for z in lauxtot:

                if w[0] == z[0]:
                    w[1]=w[1]|z[1]

        laux2=[]
        for y in range(len(lauxtot)):
            ok=True
            for z in range(y+1,len(lauxtot)):
                if lauxtot[y] == lauxtot[z]:
                    ok=False
            if ok==True:
                laux2.append(lauxtot[y])
        lauxtot=laux2
        for y in lauxtot:
            if y[1] in viz:
                continue
            else:
                viz.append(y[1])
                viitor.append(y[1])
    lauxtot.sort()
    ok=False
    for q in actual:
        if q in starefin:
            ok=True
    if ok==True:
        print(*actual,"->",*lauxtot,"STARE FINALA")
    elif starein in actual and len(actual)==1:
        print(*actual,"->",*lauxtot,"STARE INITIALA")
    else:
        print(*actual, "->", *lauxtot)


