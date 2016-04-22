import time, sys,  math

def main():
    t0 = time.clock()
    #longestChain = findLongestChain( 1000000 ) 
    longestChain = findLongestChainQuicker( 1000000 ) 
    print longestChain
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)


def findLongestChainQuicker( upper ):
    result = [ 0 ] * ( upper - 1 )
    result[ 0 ] = 1
    for i in range(2, upper):
        if result[ i - 1 ] != 0:
            continue

        n = i
        cnt = 0
        while n > upper - 1 or result[ n - 1 ] == 0:
            if n % 2 == 0:
                n = int( n / 2 )
            else:
                n = 3 * n + 1
            cnt += 1
        result[ i - 1 ] = cnt + result[ n - 1 ]
    maxIndex = 0
    maxValue = 0
    for i in range(len(result)):
        if result[ i ] > maxValue:
            maxValue = result[ i ]
            maxIndex = i
    return maxIndex         


def findLongestChain( upper ):
    ignore = set([1])
    maxLength = 0
    maxIndex = 0
    for i in range(1, upper + 1):
        if i in ignore:
            continue
        chain = chainSize(i, ignore)
        if chain > maxLength:
            maxLength = chain
            maxIndex = i
    return maxIndex

def chainSize(N, ignore):
    cnt = 1
    while N != 1:
        ignore.add(N)
        if N % 2 == 0:
            N = int( N / 2 )
        else:
            N = 3 * N + 1
        cnt += 1
    return cnt


if __name__ == '__main__':
    main()
