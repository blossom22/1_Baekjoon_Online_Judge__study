# Baekjoon_BRONZE4_4299: AFC 윔블던   

sum, sub = map(int, input().split())
if ((sum+sub)%2 != 0) or (sum<sub):     # 2로 나누어떨어지지 않으면 점수는 자연수가 아님 & 문제에서 sum이 sub보다 크다는 조건도 없었다..
    print(-1)
else:
    a = (sum+sub)//2
    b = sum-a
    print(max(a,b), min(a,b))