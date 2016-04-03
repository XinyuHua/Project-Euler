import math,sys
import time

def main():
    t0 = time.clock()
    findLargestPalindromProduct()
    t1 = time.clock()
    print 'Time elapsed: %.3f seconds' % (t1 - t0)

def findLargestPalindromProduct():
    largest = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            product = i * j
            if isPalindrom(product) and largest < product:
                largest = product
    print largest
                
def isPalindrom(target):
    targetStr = str(target)
    if targetStr[::-1] == targetStr:
        return True
    else:
        return False
        


if __name__ == "__main__":
    main() 
