# PEAK FINDING

# 1D-Array
# arr[i] is a peak IFF arr[i]>=arr[i-1] and arr[i]>=arr[i+1]
# arr[0] is a peak if arr[0]>=arr[1]
# arr[len(arr)-1] is a peak if arr[len(arr)-1]>=arr[len(arr)-2]
# peak(arr) returns a number that is a peak in the 1D array

def peak(arr):
    mid = len(arr)//2 
    if len(arr)==0:
        return "There're no items in the list"
    elif len(arr)==1:
        return str(arr[mid])+' is a peak of the list'
    elif len(arr)==2:
        if arr[1]>=arr[0]:
            return str(arr[1])+' is a peak of the list'
        else:
            return str(arr[0])+' is a peak of the list'    
    elif arr[mid]<arr[mid-1]:
        return peak(arr[:mid])
    elif arr[mid]<arr[mid+1]:
        return peak(arr[mid+1:])
    else:
        return str(arr[mid])+' is a peak of the list'




stuff = list(map(int,input().split()))
print(peak(stuff))


# 2D-Array
# arr[i][j] is a peak IFF arr[i][j]>=arr[i-1][j], arr[i+1][j], arr[i][j-1], and arr[i][j+1]
# peak2D(arr) returns a number that is a peak in the 2D array
def peak2D(arr):
    m = len(arr)//2
    if len(arr[m])==0:
        return "There're no items in the 2D-array"
    max=arr[m][0]
    maxIndex = 0
    for j in range(1,len(arr[m])):
        if arr[m][j]>max:
            max = arr[m][j]
            maxIndex = j
    #return maxIndex,max,m
    if len(arr)<=2:
        if arr[m][maxIndex]>=arr[m-1][maxIndex]:
            return str(max)+ ' is a peak of the 2D-array'
        else:
            return str(arr[m-1][maxIndex])+ ' is a peak of the 2D-array'
    elif arr[m+1][maxIndex]>arr[m][maxIndex]:
        return peak2D(arr[m+1:])
    elif arr[m-1][maxIndex]>arr[m][maxIndex]:
        return peak2D(arr[:m])
    else:
        return str(max)+ ' is a peak of the 2D-array'
    

inputs = [[1,3,5,7], [2,4,5,9],[3,7,2,1]]
print(peak2D(inputs))
inputs2 = [[1,3,5,7], [2,4,5,9],[3,7,6,11],[25,3,20,28]]
print(peak2D(inputs2))
inputs3 = [[9, 3], [5, 4], [7, 2]]
print(peak2D(inputs3))
inputs4 = [[32, 31, 30, 29], [25, 24, 23, 19], [17, 16, 13, 12], [10, 9, 7, 6]]
print(peak2D(inputs4))
inputs5 = [[1, 2, 3, 4], [9, 10, 11, 12], [19, 20, 21, 22], [28, 29, 30, 31]]
print(peak2D(inputs5))