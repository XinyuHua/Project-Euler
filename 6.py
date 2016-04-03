import math,time

def main():
    t0 = time.clock()
    brutal(1,100)
    t1 = time.clock()
    print 'Time elapsed: %.2f' % (t1 - t0)

def brutal(l,h):
    sum1 = 0
    sum2 = 0
    for i in range(l,h+1):
        sum1 += i * i
        sum2 += i
    sum2 = sum2 * sum2
    print sum2 - sum1


if __name__ == '__main__':
    main()
