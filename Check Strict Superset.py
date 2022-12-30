# Enter your code here. Read input from STDIN. Print output to STDOUT

setA = set(map(int,input().split()))
ans = True

n = int(input())

for i in range(n):
    tmp = set(map(int,input().split()))
    
    if not setA.issuperset(tmp) and len(setA) != len(tmp):
        ans = False
        
print(ans)
