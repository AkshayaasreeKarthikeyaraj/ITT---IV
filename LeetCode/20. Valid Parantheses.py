class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(" : ")", "{" : "}", "[" : "]"}
        ls = list(s)
        
        i = 0
        while i < len(ls) - 1:
            if ls[i] in d:
                if ls[i + 1] == d[ls[i]]:
                    ls.pop(i)     
                    ls.pop(i)     
                    i = 0         
                    continue      
            else:
                return False
                
            i += 1
            
        return len(ls) == 0
