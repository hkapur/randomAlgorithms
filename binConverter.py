# The binConverter class has three key functions: binToDecimal which converts Binary Numbers to Decimal notation, binToHexadecimal which converts Binary Numbers to Hexadecimal Notation, and binToOctal which converts Binary Numbers to Octal Notation
# Each returns a tuple of its notation and its respective base
# Worst Case Time Complexity of O(n)

# DecimalToBinary(num) converts an integer greater than or equal to zero to a string of binary numbers 

import math

class binConverter:
    def __init__(self,binaryNum):
        self.binaryNum = binaryNum
    def binToDecimal(self,base =10):
        n = len(self.binaryNum)
        decimal= 0
        for i in range(n-1,-1,-1):
            decimal+=(2**(n-1-i))*int(self.binaryNum[i])
        return decimal,base
    def binToHexadecimal(self,base=16):
        m = len(self.binaryNum)
        if m%4!=0:
            filledBin = '0'*(4-m%4)+self.binaryNum
        else:
            filledBin = self.binaryNum
        n = len(filledBin)
        HexNum = ''
        hexTable = {'0000':0,'0001':1,'0010':2,'0011':3,'0100':4,'0101':5,'0110':6,'0111':7,'1000':8,'1001':9,'1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
        for i in range(3,n,4):
            x = hexTable[filledBin[i-3:i+1]]
            HexNum+=str(x)
        return HexNum,base
    def binToOctal(self,base = 8):
        m = len(self.binaryNum)
        if m%3!=0:
            filledBin = '0'*(3-m%3)+self.binaryNum
        else:
            filledBin = self.binaryNum
        n = len(filledBin)
        Octal = ''
        octalTable = {'000':0,'001':1,'010':2,'011':3,'100':4,'101':5,'110':6,'111':7}
        for i in range(2,n,3):
            y = octalTable[filledBin[i-2:i+1]]
            Octal+=str(y)
        return Octal,base
                
                
def DecimalToBinary(num):
    if num==0:
        return '0'
    else:
        binary =''
        highest = int(math.log2(num))+1
        track = int(math.log2(num))+1
        while num>0:
            if not binary:
                num-=2**(int(math.log2(num)))
                binary+='1'
            elif binary:
                x = int(math.log2(num))+1
                diff = track -x-1
                track = x
                num-=2**(int(math.log2(num)))
                binary+='0'*diff
                binary+='1'
        n = len(binary)
        binary+='0'*(highest-n)
        return binary
            
            
            
        
        
            



binaryNum = input() #string of Binary Numbers
print(binConverter(binaryNum).binToDecimal())
print(binConverter(binaryNum).binToHexadecimal())
print(binConverter(binaryNum).binToOctal())
num = int(input()) # an integer >=0
print(DecimalToBinary(num))