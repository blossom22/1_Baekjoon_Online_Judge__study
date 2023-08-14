# Baekjoon_BRONZE4_28074: 모비스  

dic = {'M':0, 'O':0, 'B':0, 'I':0, 'S':0}
a = list(input())
for i in a:
    dic[i]=1
if 0 in dic.values():
    print('NO')
else:
    print('YES')