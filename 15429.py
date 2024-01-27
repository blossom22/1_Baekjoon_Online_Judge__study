# Baekjoon_Bronze3_15429: Odd Gnome

import sys
n = int(sys.stdin.readline())
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    g = data[0]
    gnome = data[1:]
    tmp = gnome[0]
    for j in range(1,g):
        if gnome[j] == tmp + 1:
            tmp = gnome[j]
        else:
            print(j+1)
            break