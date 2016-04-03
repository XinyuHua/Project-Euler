import time, sys

def main():
    t0 = time.clock()
    argument = int(sys.argv[1])
    print sumOfFibonacci_1(argument)
    t1 = time.clock()
    print "Time elapsed: %.3f sec" % (t1 - t0)

def sumOfFibonacci_1(upper):
    fibonacci = [1,2]
    sum = 2
    while fibonacci[-1] < upper:
        fibonacci.append( fibonacci[-2] + fibonacci[-1])
        print fibonacci[-1]
        if fibonacci[-1] % 2 == 0 and fibonacci[-1] <= upper:
            sum += fibonacci[-1]
    return sum

if __name__ == '__main__':
    main()
