# A way of sorting a list containing values in the set {0, 1...k}. This interested me because it is relativeley efficient O(n+k) while have a nested for loop:

def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
        p = 0
    for i in range(k + 1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A
