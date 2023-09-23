# Baekjoon_BRONZE3_6975: Deficient, Perfect, and Abundant 

import sys
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    hap = 0
    for j in range(1,a):
        if a%j==0:
            hap+=j
    if hap == a:
        print(a,'is a perfect number.')
        print()
    elif hap <a:
        print(a,'is a deficient number.')
        print()
    else:
        print(a,'is an abundant number.')
        print()