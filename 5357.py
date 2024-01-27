# Baekjoon_Bronze4_5357: Dedupe

n = int(input())
for i in range(n):
    s = input()
    ans = s[0]
    for j in range(len(s)-1):
        if s[j] != s[j+1]:
            ans += s[j+1]
    print(ans)
