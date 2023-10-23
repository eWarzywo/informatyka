def Divide(T,p,r):
    q = (p+r) // 2
    x = T[q]
    d = T[q]
    T[q] = T[r]
    T[r] = d
    j = p
    for i in range(p,r):
        if T[i] < x:
            d = T[i]
            T[i] = T[j]
            T[j] = d
            j+=1
    d = T[j]
    T[j] = T[r]
    T[r] = d
    return j

def QuickSortPart(T,p,r):
    if p < r:
        q = Divide(T,p,r)
        QuickSortPart(T,p,q)
        QuickSortPart(T,q+1,r)

def QuickSort(T):
    n = len(T)
    QuickSortPart(T,0,n-1)

T = [3,56,5,34,5,1,45,4,2,34,5,234]
QuickSort(T)
print(T)