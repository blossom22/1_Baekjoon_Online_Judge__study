# Baekjoon_CLASS2_Silver4_10816: 숫자 카드 2

from collections import defaultdict
import sys

n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))

# 딕셔너리로 바로 카운트한다. 굳이 Counter로 ml에 있지도 않은 수 까지 등장횟수를 세지말자.
ndic = defaultdict(int)
for num in nl:
    ndic[num] += 1

# 결과 계산
result = [ndic[num] for num in ml]

# 결과 출력
sys.stdout.write(' '.join(map(str, result)))