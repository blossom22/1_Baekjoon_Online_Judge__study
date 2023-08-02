# Baekjoon_BRONZE4_6825: Body Mass Index 

w = float(input())
h = float(input())
bmi = w/(h**2)
if bmi > 25:
    print('Overweight')
elif 18.5<=bmi<=25:
    print('Normal weight')
else:
    print('Underweight')