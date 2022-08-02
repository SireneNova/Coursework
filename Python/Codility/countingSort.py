# A way of sorting a list containing values in the set {0, 1...k}. This interested me because it is relativeley efficient O(n+k) while have a nested for loop.
# Kind of an odd way to write it:

def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
        p = 0
    for i in range(k + 1):
        print("i: "+ str(i))
        for j in range(count[i]):
            print("j: " + str(j))
            print("p: " + str(p))
            A[p] = i
            print(A[p])
            p += 1
    return A


A = [0,2,5,6,4,7,3,1]

print(countingSort(A, 7))
