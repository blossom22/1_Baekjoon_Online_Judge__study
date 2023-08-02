# Baekjoon_BRONZE4_4714: Lunacy      

while True:
    n = float(input())
    x = f"{n:.2f}"
    if n>=0:
        y = f"{n*0.167:.2f}"
        print(f'Objects weighing {x} on Earth will weigh {y} on the moon.')
    else:
        break