for i in range(int(input())):
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    i=0
    while i < len(nums)-1:
        if nums[i+1]-nums[i] == 1 or nums[i] == nums[i+1]:
            nums.pop(i)
            continue
        i+=1
    if len(nums) == 1:
        print('YES')
    else:
        print('NO')
