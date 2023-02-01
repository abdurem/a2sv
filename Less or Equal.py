n, k = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

ans=-1
if k == 0:
    if arr[0] > 1:
        ans = arr[0]-1

elif k == n:
    ans = arr[n-1]

elif arr[k-1] != arr[k]:
    ans = (arr[k-1]+arr[k])//2
print(ans)
