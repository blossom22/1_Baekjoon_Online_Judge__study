# Baekjoon_CLASS3_1620: 나는야 포켓몬 마스터 이다솜

import sys
n,m = map(int, sys.stdin.readline().split())
pok = {}
for i in range(n):
    j = sys.stdin.readline().strip()
    # 딕셔너리에서 update을 쓰면 기존 딕셔너리 정보를 수정하거나 새로운 값을 추가할때 유용하다. (변경하고 싶지 않은 값은 건들지 않음!)
    pok.update({j:str(i+1)})
    pok.update({str(i+1):j})
for i in range(m):
    m = sys.stdin.readline().strip()
    print(pok[m])