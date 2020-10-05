def sort(L):
    for i in range(1, len(L)):
        key = L[i]
        for j in range(i-1, -1, -1):
            if key < L[j]:
                L[j+1], L[j]  = L[j], L[j+1]
    return L
print(sort([5,3,7,1,10]))
