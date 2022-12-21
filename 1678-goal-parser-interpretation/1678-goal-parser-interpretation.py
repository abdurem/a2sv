class Solution:
    def interpret(self, command: str) -> str:
        ans=''
        stk=[]
        
        for i in range(len(command)):
            if command[i] == 'G':
                ans+='G'
            elif command[i] == '(':
                while command[i] != ')':
                    stk.append(command[i])
                    i+=1
                if stk.pop() == '(':
                    ans+='o'
                else:
                    ans+='al'
                stk.clear()
        return ans