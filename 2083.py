# Baekjoon_BRONZE4_2083: 럭비 클럽 

while True:
    a = input().split()
    if a[0] != '#':
        if int(a[1]) > 17 or int(a[2]) >=80:
            print(a[0], 'Senior')
        else:
            print(a[0], 'Junior')
    else:
        break
