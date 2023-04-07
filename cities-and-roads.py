n = int(input())
mat = []
ans=0
for i in range(n):
    mat.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if mat[i][j]:
            ans+=1

print(ans//2)