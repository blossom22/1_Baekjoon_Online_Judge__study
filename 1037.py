# Baekjoon_Bronze1_1037: 약수
# 아래 풀이도 답이 나오기는 하지만, 시간 소모가 너무 크다
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
maxx = max(nums)
for i in range(maxx+1, 1000001):
    mark = True
    for j in nums:
        if i%j!=0 or (i//j not in nums):
            mark = False
    if mark==True:
        print(i)
        break

# 그냥 정렬하고, 가장 큰 값과 가장 작은 값을 곱하면 그게 찾고자 하는 수가 된다.
# 만약 진짜 약수가 1개밖에 없다면(1과 N을 제외한 나머지 약수), 그 수만 제곱하면 답이다
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
print(nums[0]*nums[-1])