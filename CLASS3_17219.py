# Baekjoon_CLASS3_Silver4_17219: 비밀번호 찾기
# 초기에 사이트주소와 비밀번호를 해시테이블(딕셔너리)로 만들고 검색하면 된다. 
import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(n):
    a,b = sys.stdin.readline().split()
    dic[a] = b
for i in range(m):
    print(dic[sys.stdin.readline().strip()])
