H,W = map(int, input().split())
A = [list(map(int, input().split(" "))) for _ in range(H)]

sum_row = [sum(A[i]) for i in range(H)]
sum_col = [sum(A[i][j] for i in range(H)) for j in range(W)]

for i in range(H):
    for j in range(W):
        result = sum_row[i] + sum_col[j] - A[i][j]
        print(result,end=" ")
    print()