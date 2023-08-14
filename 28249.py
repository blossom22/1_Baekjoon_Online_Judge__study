# Baekjoon_BRONZE4_28249: Chili Peppers    

dic = {'Poblano':1500, 'Mirasol':6000, 'Serrano':15500, 'Cayenne':40000, 'Thai':75000, 'Habanero':125000}
n = int(input())
num = 0
for i in range(n):
    chili = input()
    num += dic[chili]
print(num)