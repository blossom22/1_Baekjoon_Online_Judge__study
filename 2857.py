# Baekjoon_BRONZE3_2857: FBI  

a = [input() for _ in range(5)]
cnt = 0
for i in a:
    if 'FBI' in i:
        print(a.index(i)+1, end=' ')
        cnt +=1
if cnt == 0:
    print('HE GOT AWAY!')

