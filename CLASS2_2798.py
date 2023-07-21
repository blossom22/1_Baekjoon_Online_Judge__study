# Baekjoon_CLASS2_2798: 블랙잭 

from itertools import combinations      # 가능합 조합을 모두 출력한다(순서고려X) 
import sys
n, m = map(int, sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

a = [sum(i) for i in list(combinations(card, 3)) if sum(i)<=m]  # 몇 개씩 구성된 조합들을 출력할건지 세팅도 가능하다
print(max(a))