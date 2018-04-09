# Memoized and Recursive Algorithm
# Worst case O(n) with Auxillary Space: O(n)
m ={}
def fib(n):
    if n in m:
        return(m[n])
    if n==0:
        m[n] = 0
    elif 0<n<=2:
        m[n] = 1
    else:    
        m[n] = fib(n-1)+fib(n-2)
    return(m[n])
print(fib(300))

#OR
# Recursive Algorithm
# Worst case O(n) with Auxillary space O(1)
def fib(i):
    if i ==0:
        return 0
    elif i==1:
        return 1+fib(i-1)
    else:
        return fib(i-1)+fib(i-2)

#Bottom-Up Algorithm (Definitely can work with more "n")
# Worst case O(n) with Auxillary Space O(n); Space Complexity O(1)


def Fib(n):
    fibNum = {}
    for i in range(n+1):
        if i==0:
            f = 0
        elif i==1:
            f = 1
        else:
            f = fibNum[i-1]+fibNum[i-2]
        fibNum[i] = f
    return(fibNum[n])
print(Fib(1000))

# Utilizing the relationship between the Golden Ratio and Conjugate and Fibonacci Numbers 
# Phi is the golden ratio and Phi-Hat is its conjugate
# Worst case O(1) with Auxillary Space O(1)
# fibGolden(i) is only accurate when i < 72

def fibGolden(i):
    phi = (1+(5**(1/2)))/2
    phiHat = (1-(5**(1/2)))/2
    num = phi**(i)-phiHat**(i)
    return int(num/(5**(1/2)))


# Sequence of Even Fibonacci Numbers 
# Worst case O(n) with Auxillary Space O(n)

def EvenFib(n):
    evenfibNum = {}
    for i in range(1,n+1):
        if i==1:
            f = 0
        elif i==2:
            f = 2
        else:
            f = 4*evenfibNum[i-1]+evenfibNum[i-2]
        evenfibNum[i] = f
    return(evenfibNum[n])
print(EvenFib(1000))

def EvenFib(n):
    evenfibNum = []
    for i in range(1,n+1):
        if i==1:
            f = 0
        elif i==2:
            f = 2
        else:
            f = 4*evenfibNum[-1]+evenfibNum[-2]
        evenfibNum+=[f]
    return evenfibNum
    #return evenfibNum[-1]
#print(*EvenFib(1000),sep='\n')
