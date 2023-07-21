# Baekjoon_CLASS2_2775: 부녀회장이 될테야 
'''
다이나믹 프로그래밍 알고리즘이 필요하다. (필요한 계산값을 저장해두었다가 재사용하는 알고리즘 기법)
다이나믹 프로그래밍 알고리즘에는 Topdown과 Bottom-up 방식이 있다.
Topdown방식은 memoization 방식을 사용(한번 구한 계산결과를 메모리공간에 적어두고, 같은 식을 재호출하면 메모결과를 그대로 가져오는 것)(재귀함수로 구현가능)
    보통 큰 문제를 해결하기 위해 작은 문제로 쪼개가면서 해결해서 하향식이라고도 한다. 
Bottom-up방식은 tabulation 방식을 사용(작은 문제들부터 해결하면서 점점 더 큰 문제를 해결하는 기법)
    상향식이라고도 부르며, '반복문'으로 구현가능
'''
# 나는 이 문제를 해결하기위해 Bottom-up방식을 사용했다. 
t = int(input())
klist = []
nlist = []
for i in range(t):
    klist.append(int(input()))
    nlist.append(int(input()))

for i in range(t):
    dp = [j for j in range(1,nlist[i]+1)]   # 작은 문제부터 해결해서 저장할 dp배열을 만든다. 처음으로 여기서 만든 dp는 제일 하위단계의 배열(1,2,3...)
    for a in range(klist[i]):
        for b in range(1,nlist[i]):         # dp[0]은 계속 1로 고정되므로 건들지 않는 것
            dp[b] = dp[b]+dp[b-1]           # 반복문으로 dp를 업데이트한다. (한층씩 높아질수록, 호수가 커질수록, dp를 증가시킨다)
    print(dp[nlist[i]-1])                   # 최종적으로 만든 dp에서, 해당하는 인덱스(호수값-1)의 dp값을 구하면 그게 곧 답이다