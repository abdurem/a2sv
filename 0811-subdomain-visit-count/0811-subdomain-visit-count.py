class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subs=defaultdict(str)
        
        for domain in cpdomains:
            dom=domain.split()
            if subs[dom[1]]:
                subs[dom[1]] = str(int(subs[dom[1]]) + int(dom[0]))
            else:
                subs[dom[1]] += dom[0]
            
            for dot in range(len(dom[1])):
                if dom[1][dot] == '.':
                    if subs[dom[1][dot+1:]]:
                        subs[dom[1][dot+1:]] = str(int(subs[dom[1][dot+1:]]) + int(dom[0]))
                    else:
                        subs[dom[1][dot+1:]] += dom[0]
                
        ans=[]
        for i in subs:
            ans.append(subs[i]+' '+i)
        
        return ans