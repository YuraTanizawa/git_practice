N = int(input())
set = set()

for i in range(N):
    s = input()
    if s in set:
        continue
    else:
        set.add(s)
        print(i+1)