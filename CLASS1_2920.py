# Baekjoon_CLASS1_2920: 음계



a = list(map(int, input().split()))
diff = [abs(a[i+1] - a[i]) for i in range(len(a)-1)]

if all(d == 1 for d in diff):       # all()내장함수는 iterable객체를 인자로 받으며, 안에 있는 것들 전부 참일때, True 반환
    if min(a) == a[0]:
        print('ascending')
    else:
        print('descending')
else:
    print('mixed')
