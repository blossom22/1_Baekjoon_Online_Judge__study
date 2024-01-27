# Baekjoon_Bronze3_11719: 그대로 출력하기 2
# EOFerror는 보통 try~except구문으로 해결한다. 참고로 EOF를 입력하려면 Ctrl + Z 누르면 된다
while True:
    try:
        a = input()
        print(a)
    except EOFError:
        break