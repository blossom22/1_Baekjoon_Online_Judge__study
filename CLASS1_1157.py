# Baekjoon_CLASS1_1157: 단어 공부

a = {}
n = input().upper()     # 전부 대문자로 바꿔서 생각하면 편하다. 어차피 결과출력도 대문자니까
for i in n:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1     # 딕셔너리 초기 세팅

max_value = max(a.values())
max_keys = [key for key,value in a.items() if value == max_value]
if len(max_keys) >1:
    print('?')
else:
    print(max_keys[0])
