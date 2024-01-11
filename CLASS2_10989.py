# Baekjoon_CLASS2_BRONZE1_10989: 수 정렬하기 3
# n(수의 개수)이 1천만까지 가서, 단순히 이들을 정렬하려고 하면 시간초과뜬다.
# 다행히, 수자체의 크기는 1만이하로 작다. 그렇다면, 0~10000번 인덱스가 담긴 배열을 만들어서 여기에 수를 카운팅해서 담자.
# 인덱스번호가 곧 수의 크기가 되고, 배열에서의 값이 수의 개수가 될테니까. 
import sys
n = int(sys.stdin.readline())
arr = [0]*10001

for i in range(n):
    num = int(sys.stdin.readline())
    arr[num]+=1
for i in range(10001):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)