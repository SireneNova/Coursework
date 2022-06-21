# This is from an example in a lesson on counting. It took me a while to wrap my head around this solution and am simply saving my comments here for reference:

def counting(A, m):
    n = len(A)
    #print ('n: ' + str(n))
    counter = [0] * (m + 1) # returns an empty array of length m, an arbitrary number
    #print ('counter: ' + str(counter))
    for k in range(n):
        #print('k: ' + str(k))
        counter[A[k]] += 1 # fills empty array count with 1 for every unit in the range of length A at the indexes of count that are values in the list A
    return counter

# m is simply the maximum number in the array
A= [6, 8, 14, 13, 8, 12, 6, 7, 7, 6, 6, 6, 6]
B = [10, 9, 8, 0, 1, 2, 3, 4, 5, 10, 1, 2, 26]
#print(counting(A, 10))
#print(sum(A))
#print(sum(B))

def fast_solution(A, B, m):
    n = len(A)
    sum_a = sum(A)
    print(sum_a)
    sum_b = sum(B)
    print(sum_b)
    d = sum_b - sum_a
    print(d)
    if d % 2 == 1:
        return False # apparently the difference has to be an even number
    d //= 2
    print(d)
    counter = counting(A, m)
    print('counter A: ' + str(counter))
    for i in range(n):
        print(i)
        if 0 <= B[i] - d and B[i] - d <= m and counter[B[i] - d] > 0:
            print('B[i] - d: ' + str(B[i] - d))
            print('count[B[i] - d]: ' + str(counter[B[i] - d]))
            return True 
            # if the value at the B index minus half the difference is positive, 
            # and the value at the B index minus half the difference is less than the maximum value
            # and there exists a value in the array that is equal to the value at the B index minus half the difference
            # return true
    return False

print(fast_solution(A, B, 26))
