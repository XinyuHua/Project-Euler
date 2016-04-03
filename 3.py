import sys,math
import time

def main():
    argument = (int(sys.argv[1]))
    t0 = time.clock()
    print 'largest prime factor of %d is %d' % (argument, largestPrimeFactor_01(argument))
    t1 = time.clock()
    print 'Time elapsed: %.3f seconds' % (t1 - t0)

def largestPrimeFactor_01(target):
    factor = 2
    lastFactor = 1
    while target > 1:
        lastFactor = factor
        while target % factor == 0:
            target = target / factor
        factor = factor + 1    
    return lastFactor
            

def largestPrimeFactor_02(target):
    m = target
    i = 2
    while i < m:
        if m % i == 0:
            m = m / i
            i = i - 1
        i = i + 1
    return m 

def isPrime(target):
    result = True
    for i in range(2,target):
        if target % i == 0:
            result = False
    return result

if __name__ == "__main__":
    main()
