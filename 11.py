import time, sys, math

def main():
    t0 = time.clock()
    g = readGrid()
    findMaxProduct( g )
    t1 = time.clock()
    print 'Time elapsed: %.3f sec' % (t1 - t0)

def readGrid():
    fin = open("20x20grid.txt","r")
    grid = [ line.split(' ') for line in fin.readlines() ]
    grid = [ map(int, row) for row in grid ]
    fin.close()
    return grid

def findMaxProduct( grid ):
    height = len(grid)
    width = len(grid[ 0 ])
    historyMax = 0
    firstCell = [ 0, 0 ]
    direction = 0;

    # 1. horizontal
    print 'Scan horizontally'
    for h in range(height):
        for w in range(width - 3):
            curProduct = grid[ h ][ w ] * grid[ h ][ w + 1 ] * grid[ h ][ w + 2 ] * grid[ h ][ w + 3 ] 
            if curProduct > historyMax:
                historyMax = curProduct
                firstCell = [ h , w ]
                direction = 0
                print 'Max updated to %d' % historyMax

    # 2. vertical 
    print 'Scan vertically'
    for w in range(width):
        for h in range(height - 3):
            curProduct = grid[ h ][ w ] * grid[ h + 1 ][ w ] * grid[ h + 2 ][ w ] * grid[ h + 3 ][ w ]
            if curProduct > historyMax:
                historyMax = curProduct
                firstCell = [ h , w ]
                direction = 1
                print 'Max updated to %d' % historyMax

           
    # 3. diagonal left-right \
    print 'Scan left-right diagonal'
    for h in range(height - 3):
        for w in range( width - 3):
            curProduct = grid[ h ][ w ] * grid[ h + 1 ][ w + 1 ] * grid[ h + 2 ][ w + 2 ] * grid[ h + 3 ][ w + 3 ]
            if curProduct > historyMax:
                historyMax = curProduct
                firstCell = [ h, w ]
                direction = 2
                print 'Max updated to %d' % historyMax


    # 4. diagonal right-left /
    print 'Scan right-left diagonal'
    for h in range(height - 3):
        for w in range(width - 1, 2, -1):
            curProduct = grid[ h ][ w ] * grid[ h + 1 ][ w - 1 ] * grid[ h + 2 ][ w - 2 ] * grid[ h + 3 ][ w - 3 ]
            if curProduct > historyMax:
                historyMax = curProduct
                firstCell = [ h, w ]
                direction = 3
                print 'Max updated to %d' % historyMax
    print historyMax
    print 'first cell:', firstCell
    print direction
    

if __name__ == '__main__':
    main()
