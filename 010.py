N = int(input())
A,B = [0]*(1+N),[0]*(1+N)
for i in range(N):
    c,p = map(int, input().split())
    if c == 1:
        B[i+1] = B[i]
        A[i+1] += p + A[i]
    elif c == 2:
        A[i+1] = A[i]
        B[i+1] += p + B[i]
        
Q = int(input())
ansA,ansB = [0]*Q,[0]*Q
for i in range(Q):
    l,r = map(int, input().split())
    ansA[i] = A[r]-A[l-1]
    ansB[i] = B[r]-B[l-1]
    
for i in range(Q):
    print(ansA[i],end=" ")
    print(ansB[i])