
def merge(A, B):
    lena = len(A)
    lenb = len(B)
    lenc = lena + lenb
    C = [0] * lenc
    i, j = 0, 0
    c = 0
    while c < lenc and j < lenb and i < lena:
        if A[i] > B[j]:
            C[c] = B[j]
            j += 1
        else:
            C[c] = A[i]
            i += 1
        c += 1
    while j < lenb:
        C[c] = B[j]
        j += 1
    while i < lena:
        C[c] = A[i]
        i += 1
    return C


def median(A):
    if len(A) % 2 == 0:
        mid1 = int(len(A) / 2) - 1
        mid2 = int(len(A) / 2)
        return (A[mid1] + A[mid2]) / 2
    else:
        mid = int(len(A) / 2)
        return A[mid]


'''
先合并，然后判断单、双，去中位数
'''

A = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]
C = merge(A, B)
print(C)
print(median(C))
