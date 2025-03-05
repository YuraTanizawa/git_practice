Q = int(input())
t,x = [],[]
ans = []
for i in range(Q):
    T,X = map(int, input().split())
    t.append(T)
    x.append(X)
    
for i in range(Q):
    if t[i] == 1:
        ans.insert(0,x[i])
    elif t[i] == 2:
        ans.append(x[i])
    else:
        print(ans[x[i]-1])