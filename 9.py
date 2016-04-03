import time, sys

def main():
    t0 = time.clock()
    ans = searchTripletProduct()
    print ans
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)

def searchTripletProduct():
    for c in range(250, 500):
        for b in range(250,c):
            a = 1000 - b - c
            if a*a + b*b == c*c:
                return a * b * c

if __name__ == '__main__':
    main()
