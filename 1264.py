# Baekjoon_BRONZE4_1264: 모음의 개수 

mo = ['a', 'e', 'i', 'o', 'u']
while True:
    a = input().lower()
    count = 0
    if a != '#':
        for i in a:
            if i in mo:
                count += 1
        print(count)
    else:
        break