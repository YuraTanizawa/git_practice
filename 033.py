H,W = map(int,input().split())
ans = 0
if H == 1 or W == 1:
    print(H*W)
    exit()
for i in range(H):
    for j in range(W):
        if i % 2 == 0 and j % 2 == 0:
            ans += 1
print(ans)