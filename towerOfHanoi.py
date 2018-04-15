# Tower Of Hanoi Mathematical game
# n circular discs of decreasing diameters stacked on one of 3 verticle pegs
# towerOfHanoi(n) outputs the minimum number of movements required to transfer the entire tower to another peg
# worst-case time complexity: O(n); Auxillary Space: O(n); Space complexity: O(n)
# Memoization method

def towerOfHanoi(n):
    T = {}
    for i in range(1,n+1):
        if i==1:
            h = 1
        else:
            h = 2*T[i-1]+1
        T[i] = h
    return T[n]

# Recursion Method
# worst-case time complexity: O(n); Auxillary Space: O(1); Space complexity: O(1)
# This method would eventually exceed maximum recursion for a certain sized n >900

def recurseTowerOfHanoi(n):
    if n==1:
        return 1
    else:
        return 2*recurseTowerOfHanoi(n-1)+1

# worst-case time complexity: O(1); Auxillary Space: O(1); Space complexity: O(1)

def towerOfHanoiFormula(n):
    return 2**(n)-1

n = int(input())    
print(towerOfHanoi(n),end='\n\n')
print(towerOfHanoiFormula(n),end='\n\n')
try:
    print(recurseTowerOfHanoi(n))
except RecursionError as r:
    print('n is too large. Pick a lower value for n:\n{}'.format(r.args[0]))
