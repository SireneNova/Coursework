#calculate the maximum number of mushrooms that the picker can collect in m moves given an array A
#containing numbers of mushrooms in each consecutive spot along a road.
#mushroom picker at spot k.
#must perform m moves

A = [2,3,7,5,1,3,9]
m = 6 #moves
k = 4 #current spot

#fills an array with sums of every slot to the left of itself and each slot of A.
def prefix_sums(A):
    length = len(A)
    P = [0] * (length + 1)
    for k in range(1, length + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def mushrooms(A, k, m):
    length = len(A)
    print("length: " + str(length))
    maxresult = 0
    pref = prefix_sums(A)
    print("A: " + str(A))
    print("P: " + str(pref))
    
    range1 = min(m, k) + 1 # min of moves (6) and position (4), + 1
    print("range1: " + str(range1)) # 5
    for p in range(range1):
        left_pos = k - p
        print("left1: " + str(left_pos))
        compright = k + (m - 2 * p)  # what is signified by m-2p?
        print("compright: " + str(compright))
        print("max k compright: " + str(max(k, compright)))
        right_pos = min(length - 1, max(k, compright)) # min of length minus 1 (6), and max of position and comp1 
        print("right1: " + str(right_pos))
        result = count_total(pref, left_pos, right_pos)
        print("result1: " + str(result))
        maxresult = max(maxresult, result)
    
    range2 = min(m + 1, length - k) # min of moves + 1 (7), and length A minus position (3)
    print("range2: " + str(range2)) # 3
    for p in range(range2):
        compleft = k - (m - 2 * p)
        print("compleft: " + str(compleft))
        print("min k compleft: " + str(min(k, compleft)))
        left_pos = max(0, min(k, compleft))
        print("left2: " + str(left_pos))
        right_pos = k + p
        print("right2: " + str(right_pos))
        result = count_total(pref, left_pos, right_pos)
        print("result2: " + str(result))
        maxresult = max(maxresult, result)
    
    return maxresult

print("number of mushrooms: " + str(mushrooms(A, k, m)))
