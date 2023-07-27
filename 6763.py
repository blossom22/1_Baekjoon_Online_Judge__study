# Baekjoon_BRONZE4_6763: Speed fines are not fine!    

a = [int(input()) for _ in range(2)]
if a[0]>=a[1]:
    print('Congratulations, you are within the speed limit!') 
elif a[0]+20>=a[1]>=a[0]+1:
    print('You are speeding and your fine is $100.')
elif a[0]+30>=a[1]>=a[0]+21:
    print('You are speeding and your fine is $270.')
else:
    print('You are speeding and your fine is $500.')