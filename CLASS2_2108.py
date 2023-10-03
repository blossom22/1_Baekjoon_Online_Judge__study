# Baekjoon_CLASS2_2108: 통계학

from collections import Counter
import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
count = Counter(a)
max_freq = max(count.values())
temp = [k for k,v in count.items() if v==max_freq]

print(round(sum(a)/n))
print(a[int(n/2)])
if len(temp)>1:
    print(temp[1])
else:
    print(temp[0])
print(max(a)-min(a))