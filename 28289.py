# Baekjoon_BRONZE3_28289: 과 조사하기

p = int(input())
soft = 0
embed = 0
ai = 0
no = 0
for i in range(p):
    g,c,n = map(int, input().split())
    if g != 1:
        if c==1 or c==2:
            soft+=1
        elif c==3:
            embed+=1
        else:
            ai+=1
    else:
        no+=1
print(soft,embed,ai,no,sep='\n')

