# Baekjoon_CLASS2_15829: Hashing 
from string import ascii_lowercase
alpha = list(ascii_lowercase)   # 알파벳 소문자들이 순서대로 들어간 리스트 출력
l = int(input())
a = [i for i in input()]

result = 0
i = 0 
for i in range(len(a)):
    result += (alpha.index(a[i])+1)*(31**i)
    i+=1
print(result%1234567891 if result>1234567891 else result) 

