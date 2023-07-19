# Baekjoon_CLASS1_3052: 나머지 

a = [(int(input())%42) for i in range(10)]
print(len(list(set(a))))        # set자료구조의 특징은 중복이 불가능하다는 점이다. set(리스트)해서 중복을 제거하고, 다시 리스트로 만들면 끝
