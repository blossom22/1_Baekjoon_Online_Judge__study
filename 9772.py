# Baekjoon_BRONZE4_9772: Quadrants 

while True:
    x,y = map(float, input().split())
    if x!=0 and y!=0:
        if x>0 and y>0:
            print('Q1')
        elif x<0 and y>0:
            print('Q2')
        elif x<0 and y<0:
            print('Q3')
        else:
            print('Q4')
    elif (x==0 and y!=0) or (x!=0 and y==0):
        print('AXIS')
    else:
        print('AXIS')
        break