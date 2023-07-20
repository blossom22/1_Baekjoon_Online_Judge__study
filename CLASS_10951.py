# Baekjoon_CLASS1_10951: A+B - 4
# 입력이 끝날때까지 출력해야한다. (End of File(EOF))
# try~except 구문(예외처리)을 이용해야 한다.

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except EOFError:        # 파일이 끝났을때, 수행
        break
