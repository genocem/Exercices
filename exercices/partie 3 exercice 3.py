def F1(L,a):

        n=65
        m = 0
        p = [0]
        g=0
        for i in L:
            if L[0]==a and g==0:
                g+=1
                continue
            elif g==0:
                g=1
            if i==a and g==1 :
                p.append   (   L.index(a, p[m]+1  ))
                m+=1
        if L[0]==a:
            n=8686
        else:
            del p[0]
        if a in L:
            return p
        else:
            return -1


