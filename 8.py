import time, sys


def main():
    t0 = time.clock()
    argument = int(sys.argv[1])
    
    ans = largestProduct(argument)
   
    print ans
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)


def largestProduct( arg ):
    f = open('1000-digit.txt', 'r')
    maxProduct = 1
    numberStr = ''
    for line in f.readlines():
        numberStr += line.strip()
    f.close()
    
    for chPtr in range( len(numberStr) - arg):
        product = 1
        for k in range(arg):
            product *= int( numberStr[chPtr + k] )
        if product > maxProduct:
            maxProduct = product
    return maxProduct
if __name__ == '__main__':
    main()
