def MinRec(T,k,l):
    if k == l:
        return T[k]
    else:
        x = MinRec(T,k,((k+l)//2))
        y = MinRec(T,((k+l)//2)+1,l)
        if x < y:
            return x
        else:
            return y
        

T = [3,7,1,4,2,5,0]
print(MinRec(T,0,len(T)-1)) 