from collections import defaultdict
tests = int(input())

for _ in range(tests):
    
    digpos = defaultdict(int)
    digneg = defaultdict(int)
    row, col = map(int,input().split())
    test=[]
    for _ in range(row):
        test.append(list(map(int,input().split())))
    
    for i in range(row):
        for j in range(col):
            digneg[i-j] += test[i][j]
            digpos[i+j] += test[i][j]
    mx=0

    for i in range(row):
        for j in range(col):
            mx = max(digneg[i-j] + digpos[i+j] - test[i][j], mx)

    print(mx)
