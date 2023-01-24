n, m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ans=[]

p=0
for i in arr2:
    if p == n:
        ans.append(str(p))
        continue
    while p < n and arr1[p] < i:
        p+=1
    ans.append(str(p))
    
print(' '.join(ans))
