# Baekjoon_CLASS1_2753: 윤년

n = int(input())
print(1) if (n%4==0 and n%100!=0) or (n%400==0) else print(0)
