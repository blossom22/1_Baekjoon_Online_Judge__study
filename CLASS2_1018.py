# Baekjoon_CLASS2_Silver4_1018: 체스판 다시 칠하기

def counting(mat, start):
    repaint = 0
    for i in range(8):
        for j in range(8):
            if mat[i][j]!=start:
                repaint+=1
            start = 'B' if start=='W' else 'W'  # 색깔을 번갈아 나오게 칠한다. 
        start = 'B' if start=='W' else 'W'
    return repaint

def finding(mat):
    min_repaint = 2500  # 초기값을 매우 큰 값으로 설정한다(N,M이 둘다 50이하이므로, 그냥 2500한 것)
    for i in range(n-7):
        for j in range(m-7):
            board = [row[j:j+8] for row in mat[i:i+8]]
            ifstart_blk = counting(board, 'B')
            ifstart_wt = counting(board, 'W')
            min_repaint = min(min_repaint, ifstart_blk, ifstart_wt)
    return min_repaint

n,m = map(int, input().split())
mat = []
for _ in range(n):
    row = list(input())
    mat.append(row)
print(finding(mat))