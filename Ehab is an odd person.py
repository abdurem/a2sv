n = int(input())

arr=list(map(int,input().split()))
ev=odd = False
for i in range(n):
    if arr[i]%2 == 1:
        odd=True
    else:
        ev=True

if ev and odd:
    arr.sort()
for i in arr:
    print(str(i), end=' ')
        
