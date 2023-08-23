# Baekjoon_BRONZE3_9317: Monitor DPI 


import sys, math
while True:
    d,rh,rv = map(float, sys.stdin.readline().split())
    if d==0 and rh==0 and rv==0:
        break
    else:
        w = 16*d/(math.sqrt(337))
        h = 9*w/16
        print('Horizontal DPI: {}'.format('{:.2f}'.format(rh/w)))
        print('Vertical DPI: {}'.format('{:.2f}'.format(rv/h)))

