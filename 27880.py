# Baekjoon_BRONZE4_27880: Gahui and Soongsil University station        

answer = 0
for i in range(4):
    a,b = map(str, input().split())
    if a == 'Es':
        answer += int(b)*21
    else:
        answer += int(b)*17
print(answer)