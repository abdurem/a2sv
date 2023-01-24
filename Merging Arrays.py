n, m = map(int,input().split())

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
ans=[]

p1=p2=0
while p1 < n or p2 < m:
    if p1 == n:
        ans.append(str(arr2[p2]))
        p2+=1
    elif p2 == m:
        ans.append(str(arr1[p1]))
        p1+=1
    elif arr1[p1] < arr2[p2]:
        ans.append(str(arr1[p1]))
        p1+=1
    else:
        ans.append(str(arr2[p2]))
        p2+=1

print(' '.join(ans))
