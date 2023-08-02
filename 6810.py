# Baekjoon_BRONZE4_6810: ISBN    

n = [9,7,8,0,9,2,1,4,1,8]
isbn = 0
for _ in range(3):
    n.append(int(input()))
for i in range(13):
    if i%2==0:
        isbn += n[i]*1
    else:
        isbn += n[i]*3
print('The 1-3-sum is {}'.format(isbn))