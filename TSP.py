"""
The code was written with the aim of finding the optimal solution to the traveling agent problem (TSP)
 - for a specific example

The data - l2 is just like l1 if switching between vertices A and B.
The tables represent distances between all 2 vertices:
for example:
    A | B | C | D | E | F
A |     x                        - x is the distance between A and B
B | x
C |
D |
E |
F |
"""

l2 = [[0, 36, 18, 26.83, 34.98, 33.94], [36, 0, 40.24, 16.97, 18.97, 26.83], [18, 40.24, 0, 24.73, 30, 24.73], [26.83, 16.97, 24.73, 0, 8.48, 12], [34.98, 18.97, 30, 8.48, 0, 8.48], [33.94, 26.83, 24.73, 12, 8.48, 0]]
l1 = [[0, 36, 40.24, 16.97, 18.97, 26.83], [36, 0, 18, 26.83, 34.98, 33.94], [40.24, 18, 0, 24.73, 30, 24.73], [16.97, 26.83, 24.73, 0, 8.48, 12], [18.97, 34.98, 30, 8.48, 0, 8.48], [26.83, 33.94, 24.73, 12, 8.48, 0]]
n = 6


def tsp_rec(lst, num):
    if num == n + 1: # we have reached depth n+1
        """At this point we get the Hamiltonian circle
            represented by a list of numbers representing rows in the distance matrix = vertex circle

            for example:
                lst = [3,2,5,1,4,0]
                the circle is D->C->F->B->E->A->back to D
        """
        global min, lmin
        i2 = lst[0] - 1
        i1 = lst[n-1] - 1
        sum = lst_tsp[i1][i2] # distance from the last to the first
        for i in range(n - 1):
            i1 = lst[i] - 1
            i2 = lst[i+1] - 1
            sum = sum + lst_tsp[i1][i2]

        if min > sum:
        # Update the minimum route if we find a shorter one
        # min = the value , lmin = the circle
            min = sum
            lmin = lst
        return

    for index in range(num): # Create מ! different routes
        arr = lst[:]
        arr.insert(index, num)
        tsp_rec(arr,num+1)

def start(enter_lst):
    global min, lmin, lst_tsp
    min = 1000  # infinity
    lmin = []
    lst_tsp = enter_lst

    tsp_rec([], 1)
    print(min, lmin)


# ------- solve ---------
lst_tsp = l1
min = 1000  # infinity
lmin = []


start(l1)
start(l2)


"""
UOTPUT:
112.66 [4, 5, 6, 3, 2, 1]
112.66 [6, 5, 4, 2, 1, 3]

Process finished with exit code 0
"""