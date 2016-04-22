import time, sys,  math

def main():
    t0 = time.clock()
    quickSum(10) 
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)


def dumbMethod():
    print sum( readData() )


# only sum the first N digits
def quickSum(N):
    fin = open('one-hundred-50-digit-numbers.txt','r')
    buckets = [ long( line[:N + 2] ) for line in fin.readlines() ]
    fin.close()
    print sum(buckets)

def readData():
    fin = open('one-hundred-50-digit-numbers.txt','r')
    buckets = [ long(line) for line in fin.readlines() ]
    fin.close()
    return buckets

if __name__ == '__main__':
    main()
