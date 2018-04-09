# powerSets(a,n) returns an array with the sets of all subsets in set a
# n represents the length of a 
# Powersets of any set a will have a length of 2^n.
# This is a prototype algorithm until I figure out a better method

def powerSets(a,n):
    stack = [[]]
    return duplicate(a,stack,n,0)
def distribute(o,stack,arr):
    for x in range(len(stack)):
        arr.append(list(stack[x]))
        arr[x]+=o
    return arr
def duplicate(a,stack,n,i):
    if i==n:
        return stack
    else:
        z = []
        y = [a[i]]
        j = distribute(y,stack,z)
        stack+=j
        return duplicate(a,stack,n,i+1)





    
    
        
n = int(input())
a = list(map(str,input().split()))
#22
#a b c d e f g h i j k l m n o p q r s t u v
print(powerSets(a,n))
print(len(powerSets(a,n)))