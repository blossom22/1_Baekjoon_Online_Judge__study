# Baekjoon_CLASS1_1157: 단어 공부

a = {}
n = input().upper()     # 전부 대문자로 만들면 카운트하기도 쉽다
for i in n:
    if i not in a:
        a[i] = 1    
    else:
        a[i] += 1       # 문자 개수 세서 딕셔너리에 추가한다

b = list(a.values())
max_value = max(b)
max_keys = [key for key, value in a.items() if value == max_value]

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])
