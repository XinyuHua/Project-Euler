import math,sys
import time

def main():
    t0 = time.clock()
    findSmallestMultiple(1,20)
    t1 = time.clock()
    print 'Time elapsed: %.3f seconds' % (t1 - t0)

def findSmallestMultiple(l, h):
    product = 1
    for i in range(l,h + 1):
        gcdN = gcd(i, product)
        print 'i = %d product = %d gcd(%d, %d) = %d' % (i,product,i,product,gcdN)
        product = product * (i / gcdN)
    print product

def gcd(a,b):
    if a == 0:
        return b
    if b == 0:
        return a 

    if a > b:
        print 'a = %d b = %d' % (a, b)
        return gcd( b, a %  b )
    elif a < b:
        print 'a = %d b = %d' % (a, b)
        return gcd( a, b %  a )
    else:
        return a

if __name__ == "__main__":
    main() 
