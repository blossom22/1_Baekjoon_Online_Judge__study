# Baekjoon_BRONZE1_2309: 일곱 난쟁이 
# 일단 아홉명의 키를 전부 더해서, 100을 뺀 후, 그 차이가 아홉명에서 조합에서 두 수의 합으로 나올수있나 two-pointer로 보자. 
data = [int(input()) for _ in range(9)]
a = sum(data)-100
data.sort()
left, right = 0,len(data)-1
while True:
    hap = data[left] + data[right]
    if hap == a:
        temp = [data[left], data[right]]
        break
    elif hap>a:
        right-=1
    else:
        left+=1
for i in data:
    if i not in temp:
        print(i)