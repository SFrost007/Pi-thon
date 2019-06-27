#!/usr/bin/env python

import copy, random, sys, time
import scrollphathd as sphd

def scroll_life(delay):
    def count_neighbours(ibuf, i, j):
        tot=0
        for x,y in ((-1,-1), (-1,0), (-1,1),
                    ( 0,-1)         , (0,1),
                    (+1,-1), (+1,0), (+1,1)):
            ix=(i+x)%11
            jy=(j+y)%5
            tot+=ibuf[ix][jy]
        return tot
    
    def buffer(ibuf):
        return [ibuf2buf[tuple(v)] for v in ibuf]
    
    def rand_ibuf():
        return [[(random.random()>0.8)+0 for j in range(7)] for i in range(17)]

    def display_buf(ibuf):
        print("Outputting:")
        for x in range(17):
            for y in range(7):
                sphd.set_pixel(x,y,ibuf[x][y])
                sys.stdout.write('#' if ibuf[x][y] else ' ')
            sys.stdout.write('\n')
            sys.stdout.flush()
        sphd.show()

    def glider_ibuf():
        return [[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]]
    
    ibuf=glider_ibuf()
    display_buf(ibuf)
    time.sleep(4)
    samecount=0
    while True:
        ibufbuf=copy.deepcopy(ibuf)
        for i in range(17):
            for j in range(7):
                c=count_neighbours(ibufbuf, i, j)
                if ibuf[i][j]:
                    if c in (0,1,4,5,6,7):
                        print("Killing %d, %d" % (i, j))
                        ibuf[i][j]=0
                else:
                    if c in (3,):
                        print("Spawning %d, %d" % (i,j))
                        ibuf[i][j]=1
        display_buf(ibuf)
        time.sleep(delay)
        if ibufbuf==ibuf:
            samecount+=1
        if samecount>20:
            ibuf=rand_ibuf()
            
if __name__== "__main__":
    scroll_life(1)
