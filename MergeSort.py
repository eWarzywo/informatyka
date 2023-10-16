# Program w języku Python do implementacji sortowania przez scalanie

# Łączy dwa podtablice arr[].
# Pierwsza podtablica to arr[l..m]
# Druga podtablica to arr[m+1..r]

def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # tworzenie tablic tymczasowych
    L = [0] * (n1)
    R = [0] * (n2)

    # Kopiowanie danych do tablic tymczasowych L[] i R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Łączenie tablic tymczasowych z powrotem do arr[l..r]
    i = 0  # początkowy indeks pierwszej podtablicy
    j = 0  # początkowy indeks drugiej podtablicy
    k = l  # początkowy indeks scalonej podtablicy

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Kopiowanie pozostałych elementów z L[], jeśli takie istnieją
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Kopiowanie pozostałych elementów z R[], jeśli takie istnieją
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l to indeks lewej strony, a r to indeks prawej strony podtablicy arr do posortowania

def MergeSortPart(arr, l, r):
    if l < r:

        # To samo co (l+r)//2, ale unika przepełnienia dla dużych wartości l i h
        m = l+(r-l)//2

        # Sortowanie pierwszej i drugiej połowy
        MergeSortPart(arr, l, m)
        MergeSortPart(arr, m+1, r)
        Merge(arr, l, m, r)


def MergeSort(arr):
    MergeSortPart(arr, 0, len(arr)-1)


# Kod sterujący do testowania powyższego algorytmu
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Dana tablica to")
for i in range(n):
    print("%d" % arr[i],end=" ")

MergeSort(arr)

print("\n\nPosortowana tablica to")
for i in range(n):
    print("%d" % arr[i],end=" ")