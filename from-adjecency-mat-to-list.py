from collections import defaultdict

d = defaultdict(list)
n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if mat[i][j]:
            d[i+1].append(str(j+1))
for i in d:
    print(len(d[i]),' '.join(d[i]))