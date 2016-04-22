import time, sys,  math

def main():
    t0 = time.clock()
    findTriNumberWithDivisorNum(int( sys.argv[1] )  )
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)

def findTriNumberWithDivisorNum( number ):
    triNum = 1
    i = 2
    divNum = divisorNum(triNum)
    while divNum < number:
        triNum += i
        i += 1
        divNum = divisorNum(triNum)
        print '%d\t%d\t%d' % (i, triNum, divNum)
    print triNum    

def divisorNum( number ):
    cnt = 0
    for i in range(1,int(math.ceil( math.sqrt(number))) ):
        if number % i == 0:
            cnt += 1
    cnt *= 2
    if math.sqrt(number) == math.ceil( math.sqrt(number) ):
        cnt += 1
    return cnt

if __name__ == '__main__':
    main()
