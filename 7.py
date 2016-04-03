import time, sys, math


def main():
    t0 = time.clock()
    argument = int(sys.argv[1])
    ans = NthPrime(argument)
   # ans = isPrime(argument)
    print ans
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)

def NthPrime(N):
    cnt = 1
    i = 3
    while cnt < N:
        if isPrime(i):
#            print i
            cnt += 1
        i += 2
    return i - 2

def isPrime(N):
    if N < 4:
        return True
    if N % 2 == 0:
        return False
    upper = int(math.ceil(math.sqrt(N)))
    for i in range(3, upper + 1, 2):
        if N % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()
