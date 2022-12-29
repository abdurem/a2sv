if __name__ == '__main__':
    N = int(input())
    ops=[]
    
    for i in range(N):
        ops.append(input().split())
        
    ans=[]
    for acts in ops:
        if acts[0] == 'append':
            ans.append(int(acts[1]))
        elif acts[0] == 'print':
            print(ans)
        elif acts[0] == 'remove':
            ans.remove(int(acts[1]))
        elif acts[0] == 'insert':
            ans.insert(int(acts[1]),int(acts[2]))
        elif acts[0] == 'sort':
            ans.sort()
        elif acts[0] == 'reverse':
            ans.reverse()
        else:
            ans.pop()
    
    # print(ans)
