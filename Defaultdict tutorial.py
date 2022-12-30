from collections import defaultdict

d=defaultdict(list)
lenA, lenB=map(int,input().split())
GroupA=defaultdict(list)
GroupB=[]

for i in range(lenA):
    GroupA[input()].append(str(i+1))
for j in range(lenB):
    GroupB.append(input())

for i in GroupB:
    if not GroupA[i]:
        print(-1)
        continue
    print(' '.join(GroupA[i]))
