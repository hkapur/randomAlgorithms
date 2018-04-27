# strassenAlg(A,B) returns the product of the two nXn matrices A and B (Strassen's Algorithm)
# makingMatricesaPowerOf2(n,A,B) is used to convert both A and B into matrices who's size n is a power of 2 so that partitioning in strassenAlg(A,B) is feasible
# Worst-Case Time complexity of O(n^(lg2(7)))
# Auxillary Space O(n^(2)) 
# Space Complexity O(n^(2))

from math import log2

def strassenAlg(A,B):
    n = len(A)
    if n ==1:
        return A[0][0]*B[0][0]
    else:
        C = [[0 for j in range(n)] for i in range(n)]
        m = n//2
        A11 = [[A[i][j] for j in range(m)] for i in range(m)]
        A12 = [[A[i][j] for j in range(m,n)] for i in range(m)]
        A21 = [[A[i][j] for j in range(m)] for i in range(m,n)]
        A22 = [[A[i][j] for j in range(m,n)] for i in range(m,n)]
        B11 = [[B[i][j] for j in range(m)] for i in range(m)]
        B12 = [[B[i][j] for j in range(m,n)] for i in range(m)]
        B21 = [[B[i][j] for j in range(m)] for i in range(m,n)]
        B22 = [[B[i][j] for j in range(m,n)] for i in range(m,n)]
        S1 = [[B12[i][j]-B22[i][j] for j in range(m)] for i in range(m)]
        S2 = [[A11[i][j]+A12[i][j] for j in range(m)] for i in range(m)]
        S3 = [[A21[i][j]+A22[i][j] for j in range(m)] for i in range(m)]
        S4 = [[B21[i][j]-B11[i][j] for j in range(m)] for i in range(m)]
        S5 = [[A11[i][j]+A22[i][j] for j in range(m)] for i in range(m)]
        S6 = [[B11[i][j]+B22[i][j] for j in range(m)] for i in range(m)]
        S7 = [[A12[i][j]-A22[i][j] for j in range(m)] for i in range(m)]
        S8 = [[B21[i][j]+B22[i][j] for j in range(m)] for i in range(m)]
        S9 = [[A11[i][j]-A21[i][j] for j in range(m)] for i in range(m)]
        S10 =[[B11[i][j]+B12[i][j] for j in range(m)] for i in range(m)]
        P1 = strassenAlg(A11,S1)
        P2 = strassenAlg(S2,B22)
        P3 = strassenAlg(S3,B11)
        P4 = strassenAlg(A22,S4)
        P5 = strassenAlg(S5,S6)
        P6 = strassenAlg(S7,S8)
        P7 = strassenAlg(S9,S10)
        if isinstance(P1,list) and isinstance(P2,list) and isinstance(P3,list) and isinstance(P4,list) and isinstance(P5,list) and isinstance(P6,list) and isinstance(P7,list):
            for i in range(m):
                for j in range(m):
                    C[i][j] = P5[i][j]+P4[i][j]-P2[i][j]+P6[i][j]
                    C[i][m+j] = P1[i][j] + P2[i][j]
                    C[m+i][j] = P3[i][j] + P4[i][j]
                    C[m+i][m+j] = P5[i][j] + P1[i][j] - P3[i][j] - P7[i][j]
        else:
            for i in range(m):
                for j in range(m):
                    C[i][j] = P5+P4-P2+P6
                    C[i][m+j] = P1 + P2
                    C[m+i][j] = P3 + P4
                    C[m+i][m+j] = P5 + P1 - P3 - P7
        return C

def makingMatricesaPowerOf2(n,A,B):
    if log2(n)==int(log2(n)):
        for i in range(n):
            A.append(list(map(int,input().split())))
            B.append(list(map(int,input().split())))
    else:
        for i in range(n):
            A.append(list(map(int,input().split()))+[0]*(2**(int(log2(n))+1)-n))
            B.append(list(map(int,input().split()))+[0]*(2**(int(log2(n))+1)-n))
        for i in range(2**(int(log2(n))+1)-n):
            A.append([0 for i in range(2**(int(log2(n))+1))])
            B.append([0 for i in range(2**(int(log2(n))+1))])
    

n = int(input())
A = []
B = []
makingMatricesaPowerOf2(n,A,B)
print('A',*A,sep = '\n',end = '\n\n\n')
print('B',*B,sep='\n', end = '\n\n\n')
C = [[strassenAlg(A,B)[i][j] for j in range(n)] for i in range(n)]
print('C',*C,sep='\n' )
