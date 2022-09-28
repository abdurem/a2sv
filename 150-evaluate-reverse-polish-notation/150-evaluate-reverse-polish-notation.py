class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp=['+','-','*','/']
        ans=0
        que=[]
        
        for i in range(len(tokens)):
            if tokens[i] not in exp:
                que.append(int(tokens[i]))
                continue
            tmp1=que[-2]
            tmp2=que[-1]
            que.pop(-1)
            que.pop(-1)
            if tokens[i] == '+':
                que.append(tmp1+tmp2)
            elif tokens[i] == '-':
                que.append(tmp1-tmp2)
            elif tokens[i] == '*':
                que.append(tmp1*tmp2)
            else:
                que.append(int(tmp1/tmp2))
        
        return que[0]