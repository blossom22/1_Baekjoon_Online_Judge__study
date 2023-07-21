# Baekjoon_CLASS2_2869: 달팽이는 올라가고 싶다 

def snail(A, B, V):
    days = (V - B - 1) // (A - B) + 1   # 1을 더하는 이유는 나눴을때 소수점이하가 생길 수 있어서
    # V-B는 정상 도달하기 바로 직전 날까지 올라간 높이(미끄러지기 전). 그런데 여기서 V-B-1인 이유는 마지막날에는 낮에 A미터만큼 올라가서 미끄러지지 않고 정상도달하기 때문에 1일을 빼줘야 된다.
    # A-B는 하루에 올라갈 수 있는 높이
    return days

A, B, V = map(int, input().split())

result = snail(A, B, V)
print(result)
