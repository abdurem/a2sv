for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    ans=0
    sign=True
    if arr[0] < 0:
        sign=False
    i=0
    
    while i < n:
        pos=0
        neg=0   
        while not sign and i < n and arr[i] < 0:
            if neg == 0:
                neg=arr[i]
            else:
                neg = max(neg,arr[i])
            i+=1
        while sign and i < n and arr[i] > 0:
            pos = max(pos,arr[i])
            i+=1
        if sign:
            ans+=pos
            sign = False
        else:
            ans+=neg
            sign = True
    print(ans)
        
