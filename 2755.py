# Baekjoon_Bronze1_2755: 이번학기 평점은 몇점?

import sys
grade = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
n = int(sys.stdin.readline())
score = 0
hap = 0
tmp = [list(map(str, sys.stdin.readline().split()))[1:] for _ in range(n)]
for i in tmp:
    score += int(i[0])*grade[i[1]]
    hap += int(i[0])
# 그냥 round를 쓰자니, 제대로 반올림이 되지 않는다(사사오입문제등등...3.275인데 반올림결과가 3.27로 나옴.)
# 따라서 소수에서 해결하지말고 1000을 곱해서 정수형으로 바꾼후, 일의자리에서 반올림하고, 마지막에 다시 소수형으로 바꾸는게 맘 편하다.
# 물론 f-string으로 소수점 두자리는 맞춰줘야 한다(문제조건)
print(f"{(round(score/hap*1000, -1)/1000):.2f}")