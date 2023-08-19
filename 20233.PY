# Baekjoon_BRONZE4_20233: Bicycle   

a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

i = (t-30)*x*21 + a
j = (t-45)*y*21 + b
if t<30:
    print(a,b,sep=' ')
elif 30<=t<45:
    print(i,b,sep=' ')
else:
    print(i,j,sep=' ')